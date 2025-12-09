from __future__ import annotations

import datetime as dt
import getpass
import logging
import re
import time
from collections.abc import Iterable
from contextlib import contextmanager
from datetime import (
    datetime,
    timedelta,
)
from typing import Any

import tenacity
from tenacity import (
    TryAgain,
    retry,
)
from tenacity.retry import retry_if_exception
from tenacity.stop import stop_after_delay
from tenacity.wait import wait_fixed

from exasol.saas.client import (
    Limits,
    openapi,
)
from exasol.saas.client.openapi.api.clusters import (
    get_cluster_connection,
    list_clusters,
)
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    get_database,
    list_databases,
)
from exasol.saas.client.openapi.api.security import (
    add_allowed_ip,
    delete_allowed_ip,
    list_allowed_i_ps,
)
from exasol.saas.client.openapi.errors import UnexpectedStatus
from exasol.saas.client.openapi.models.exasol_database import ExasolDatabase
from exasol.saas.client.openapi.models.status import Status
from exasol.saas.client.openapi.types import UNSET

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    datefmt="[%X]",
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def interval_retry(interval: timedelta, timeout: timedelta):
    return tenacity.retry(wait=wait_fixed(interval), stop=stop_after_delay(timeout))


def timestamp_name(project_short_tag: str | None = None) -> str:
    """
    project_short_tag: Abbreviation of your project
    """
    timestamp = f"{datetime.utcnow().timestamp():.0f}"
    owner = getpass.getuser()
    candidate = f"{timestamp}{project_short_tag or ''}-{owner}"
    return candidate[: Limits.MAX_DATABASE_NAME_LENGTH]


RETRY_PATTERN = re.compile("Operation.*not allowed.*cluster.*not.*in.*proper state")


def indicates_retry(ex: BaseException) -> bool:
    """
    Check whether an the specified exception raised during deleting a
    database instance indicates to retry deletion.
    """
    return bool(
        isinstance(ex, UnexpectedStatus)
        and ex.status_code == 400
        and RETRY_PATTERN.search(ex.content.decode("utf-8"))
    )


class DatabaseStartupFailure(Exception):
    """
    If a SaaS database instance during startup reports a status other than
    successful.
    """


class DatabaseDeleteTimeout(Exception):
    """
    If deletion of a SaaS database instance was requested but during the
    specified timeout it was still reported in the list of existing databases.
    """


def create_saas_client(
    host: str,
    pat: str,
    raise_on_unexpected_status: bool = True,
) -> openapi.AuthenticatedClient:
    return openapi.AuthenticatedClient(
        base_url=host,
        token=pat,
        raise_on_unexpected_status=raise_on_unexpected_status,
    )


def _get_database_id(
    account_id: str,
    client: openapi.AuthenticatedClient,
    database_name: str,
) -> str:
    """
    Finds the database id, given the database name.
    """
    dbs = list_databases.sync(account_id, client=client)
    dbs = list(
        filter(
            lambda db: (db.name == database_name)  # type: ignore
            and (db.deleted_at is UNSET)  # type: ignore
            and (db.deleted_by is UNSET),
            dbs,  # type: ignore
        )
    )  # type: ignore
    if not dbs:
        raise RuntimeError(f"SaaS database {database_name} was not found.")
    return dbs[0].id


def get_database_id(
    host: str,
    account_id: str,
    pat: str,
    database_name: str,
) -> str:
    """
    Finds the database id, given the database name.

    Args:
        host:           SaaS service URL.
        account_id:     User account ID
        pat:            Personal Access Token.
        database_name:  Database name.
    """
    with create_saas_client(host, pat) as client:
        return _get_database_id(account_id, client, database_name)


def get_connection_params(
    host: str,
    account_id: str,
    pat: str,
    database_id: str | None = None,
    database_name: str | None = None,
) -> dict[str, Any]:
    """
    Gets the database connection parameters, such as those required by pyexasol:
    - dns
    - user
    - password.
    Returns the parameters in a dictionary that can be used as kwargs when
    creating a connection, like in the code below:

    connection_params = get_connection_params(...)
    connection = pyexasol.connect(**connection_params)

    Args:
        host:           SaaS service URL.
        account_id:     User account ID
        pat:            Personal Access Token.
        database_id:    Database ID, id known.
        database_name:  Database name, in case the id is unknown.
    """

    with create_saas_client(host, pat) as client:
        if not database_id:
            if not database_name:
                raise ValueError(
                    "To get SaaS connection parameters, "
                    "either database name or database id must be provided."
                )
            database_id = _get_database_id(
                account_id, client, database_name=database_name
            )
        clusters = list_clusters.sync(account_id, database_id, client=client)
        cluster_id = next(
            filter(lambda cl: cl.main_cluster, clusters)  # type: ignore
        ).id
        connections = get_cluster_connection.sync(
            account_id, database_id, cluster_id, client=client
        )
        if connections is None:
            raise RuntimeError("Failed to get the SaaS connection data.")
        connection_params = {
            "dsn": f"{connections.dns}:{connections.port}",
            "user": connections.db_username,
            "password": pat,
        }
        return connection_params


class OpenApiAccess:
    """
    This class is meant to be used only in the context of the API
    generator repository while integration tests in other repositories are
    planned to only use fixture ``saas_database_id()``.
    """

    def __init__(self, client: openapi.AuthenticatedClient, account_id: str):
        self._client = client
        self._account_id = account_id

    def create_database(
        self,
        name: str,
        cluster_size: str = "XS",
        region: str = "eu-central-1",
        idle_time: timedelta | None = None,
    ) -> ExasolDatabase | None:
        def minutes(x: timedelta) -> int:
            return x.seconds // 60

        idle_time = idle_time or Limits.AUTOSTOP_MIN_IDLE_TIME
        cluster_spec = openapi.models.CreateDatabaseInitialCluster(
            name="my-cluster",
            size=cluster_size,
            auto_stop=openapi.models.AutoStop(
                enabled=True,
                idle_time=minutes(idle_time),
            ),
        )
        LOG.info("Creating database %s", name)
        return create_database.sync(
            self._account_id,
            client=self._client,
            body=openapi.models.CreateDatabase(
                name=name,
                initial_cluster=cluster_spec,
                provider="aws",
                region=region,
                stream_type="feature-release",
            ),
        )

    @contextmanager
    def _ignore_failures(self, ignore: bool = False):
        before = self._client.raise_on_unexpected_status
        self._client.raise_on_unexpected_status = not ignore
        yield self._client
        self._client.raise_on_unexpected_status = before

    def wait_until_deleted(
        self,
        database_id: str,
        timeout: timedelta = timedelta(seconds=1),
        interval: timedelta = timedelta(minutes=1),
    ):
        @interval_retry(interval, timeout)
        def still_exists() -> bool:
            result = database_id in self.list_database_ids()
            if result:
                raise TryAgain
            return result

        if still_exists():
            raise DatabaseDeleteTimeout

    def delete_database(
        self,
        database_id: str,
        ignore_failures: bool = False,
        timeout: timedelta = timedelta(minutes=5),
        interval: timedelta = timedelta(seconds=1),
    ) -> None:
        @retry(
            reraise=True,
            wait=wait_fixed(interval),
            stop=stop_after_delay(timeout),
            retry=retry_if_exception(indicates_retry),
        )
        def delete_with_retry():
            delete_database.sync_detailed(self._account_id, database_id)

        try:
            delete_with_retry()
        except Exception as ex:
            if ignore_failures:
                LOG.error(
                    f"Ignoring failure when deleting database with ID %s: %s",
                    database_id,
                    ex,
                )
            else:
                raise

    def list_database_ids(self) -> Iterable[str]:
        dbs = list_databases.sync(self._account_id, client=self._client) or []
        return (db.id for db in dbs)

    @contextmanager
    def database(
        self,
        name: str,
        keep: bool = False,
        ignore_delete_failure: bool = False,
        idle_time: timedelta | None = None,
    ):
        db = None
        start = datetime.now()
        try:
            db = self.create_database(name, idle_time=idle_time)
            yield db
        finally:
            db_repr = f"{db.name} with ID {db.id}" if db else None
            if not db:
                LOG.warning("Cannot delete database None")
            elif keep:
                LOG.info("Keeping database %s as keep = %s.", db_repr, keep)
            else:
                LOG.info("Deleting database %s", db_repr)
                self.delete_database(db.id, ignore_delete_failure)
                LOG.info("Successfully deleted database %s.", db_repr)

    def get_database(self, database_id: str) -> ExasolDatabase | None:
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
    ):
        success = [Status.RUNNING]

        @interval_retry(interval, timeout)
        def poll_status() -> Status:
            db = self.get_database(database_id)
            status = db.status if db else None
            if status not in success:
                LOG.info("- Database status: %s ...", status)
                raise TryAgain
            return status

        if poll_status() not in success:
            raise DatabaseStartupFailure()

    def clusters(
        self,
        database_id: str,
    ) -> list[openapi.models.Cluster] | None:
        return list_clusters.sync(
            self._account_id,
            database_id,
            client=self._client,
        )

    def get_connection(
        self,
        database_id: str,
        cluster_id: str,
    ) -> openapi.models.ClusterConnection | None:
        return get_cluster_connection.sync(
            self._account_id,
            database_id,
            cluster_id,
            client=self._client,
        )

    def list_allowed_ip_ids(self) -> Iterable[str]:
        ips = (
            list_allowed_i_ps.sync(
                self._account_id,
                client=self._client,
            )
            or []
        )
        return (x.id for x in ips)

    def add_allowed_ip(
        self,
        cidr_ip: str = "0.0.0.0/0",
    ) -> openapi.models.allowed_ip.AllowedIP | None:
        """
        Suggested values for cidr_ip:
        * 185.17.207.78/32
        * 0.0.0.0/0 = all ipv4
        * ::/0 = all ipv6
        """
        rule = openapi.models.CreateAllowedIP(
            name=timestamp_name(),
            cidr_ip=cidr_ip,
        )
        return add_allowed_ip.sync(
            self._account_id,
            client=self._client,
            body=rule,
        )

    def delete_allowed_ip(self, id: str, ignore_failures=False):
        with self._ignore_failures(ignore_failures) as client:
            return delete_allowed_ip.sync_detailed(self._account_id, id, client=client)

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
