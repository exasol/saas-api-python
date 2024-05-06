import getpass
import logging
import time

from typing import Iterable
from contextlib import contextmanager
from datetime import datetime, timedelta
from tenacity.wait import wait_fixed
from tenacity.stop import stop_after_delay

from exasol.saas.client import openapi
from exasol.saas.client.openapi.models.status import Status
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    list_databases,
    get_database,
)
from exasol.saas.client.openapi.api.security import (
    list_allowed_i_ps,
    add_allowed_ip,
    delete_allowed_ip,
)
from tenacity import retry, TryAgain


LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


# For auto-stopping idle database clusters
MINIMUM_IDLE_TIME = timedelta(minutes=15)


# If deleting a database too early, then logging and accounting could be invalid.
MINIMUM_LIFETIME = timedelta(seconds=30)


def _timestamp_name() -> str:
    username = getpass.getuser()
    timestamp = f'{datetime.now().timestamp():.0f}'
    return f"{username}-{timestamp}"


class DatabaseStartupFailure(Exception):
    """
    If a SaaS database instance during startup reports a status other than
    successful.
    """


def create_saas_client(
        host: str,
        pat: str,
        raise_on_unexpected_status: bool = True,
) -> openapi.AuthenticatedClient:
    return openapi.AuthenticatedClient(
        base_url=host,
        token=pat,
        raise_on_unexpected_status = raise_on_unexpected_status,
    )


class _OpenApiAccess:
    """
    This class is meant to be used only in the context of the API
    generator repository while integration tests in other repositories are
    planned to only use fixture ``saas_database_id()``.
    """

    def __init__(self, client: openapi.Client, account_id: str):
        self._client = client
        self._account_id = account_id

    def create_database(self, cluster_size: str = "XS") -> openapi.models.database.Database:
        cluster_spec = openapi.models.CreateCluster(
            name="my-cluster",
            size=cluster_size,
            auto_stop=openapi.models.AutoStop(
                enabled=True,
                idle_time=int(MINIMUM_IDLE_TIME.seconds / 60),
            ),
        )
        db_name = _timestamp_name()
        LOG.info(f"Creating database {db_name}")
        return create_database.sync(
            self._account_id,
            client=self._client,
            body=openapi.models.CreateDatabase(
                name=db_name,
                initial_cluster=cluster_spec,
                provider="aws",
                region='us-east-1',
            )
        )

    @contextmanager
    def _ignore_failures(self, ignore: bool = False):
        before = self._client.raise_on_unexpected_status
        self._client.raise_on_unexpected_status = not ignore
        yield self._client
        self._client.raise_on_unexpected_status = before

    def delete_database(self, database_id: str, ignore_failures=False):
        with self._ignore_failures(ignore_failures) as client:
            return delete_database.sync_detailed(
                self._account_id, database_id, client=client)

    def list_database_ids(self) -> Iterable[str]:
        dbs = list_databases.sync(self._account_id, client=self._client)
        return (db.id for db in dbs)

    @contextmanager
    def database(
            self,
            keep: bool = False,
            ignore_delete_failure: bool = False,
    ):
        db = None
        start = datetime.now()
        try:
            db = self.create_database()
            yield db
            self.wait_for_delete_clearance(start)
        finally:
            if db and not keep:
                LOG.info(f"Deleting database {db.name}")
                response = self.delete_database(db.id, ignore_delete_failure)
                if response.status_code == 200:
                    LOG.info(f"Successfully deleted database {db.name}.")
                else:
                    LOG.info(f"Ignoring status code {response.status_code}.")
            elif not db:
                LOG.warning("Cannot delete db None")
            else:
                LOG.info(f"Keeping database {db.name} as keep = {keep}")

    def get_database(self, database_id: str) -> openapi.models.database.Database:
        return get_database.sync(
            self._account_id,
            database_id,
            client=self._client,
        )

    def wait_until_running(
            self,
            database_id: str,
            timeout: timedelta = timedelta(minutes=30),
            interval: timedelta = timedelta(minutes=2),
    ) -> str:
        success = [
            Status.RUNNING,
        ]

        @retry(wait=wait_fixed(interval), stop=stop_after_delay(timeout))
        def poll_status():
            db = self.get_database(database_id)
            if db.status not in success:
                print(f'status = {db.status}')
                raise TryAgain
            return db.status

        if poll_status() not in success:
            raise DatabaseStartupFailure()


    def list_allowed_ip_ids(self) -> Iterable[openapi.models.allowed_ip.AllowedIP]:
        ips = list_allowed_i_ps.sync(
            self._account_id,
            client=self._client,
        )
        return (x.id for x in ips)

    def wait_for_delete_clearance(self, start: datetime.time):
        lifetime = datetime.now() - start
        if lifetime < MINIMUM_LIFETIME:
            wait = MINIMUM_LIFETIME - lifetime
            LOG.info(f"Waiting {int(wait.seconds)} seconds"
                     " before deleting the database.")
            time.sleep(wait.seconds)

    def add_allowed_ip(self, cidr_ip: str = "0.0.0.0/0") -> openapi.models.allowed_ip.AllowedIP:
        """
        Suggested values for cidr_ip:
        * 185.17.207.78/32
        * 0.0.0.0/0 = all ipv4
        * ::/0 = all ipv6
        """
        rule = openapi.models.create_allowed_ip.CreateAllowedIP(
            name=_timestamp_name(),
            cidr_ip=cidr_ip,
        )
        return add_allowed_ip.sync(
            self._account_id,
            client=self._client,
            body=rule,
        )

    def delete_allowed_ip(self, id: str, ignore_failures=False):
        with self._ignore_failures(ignore_failures) as client:
            return delete_allowed_ip.sync_detailed(
                self._account_id, id, client=client)

    @contextmanager
    def allowed_ip(
            self,
            cidr_ip: str = "0.0.0.0/0",
            keep: bool = False,
            ignore_delete_failure: bool = False,
    ):
        ip = None
        try:
            ip = self.add_allowed_ip(cidr_ip)
            yield ip
        finally:
            if ip and not keep:
                self.delete_allowed_ip(ip.id, ignore_delete_failure)
