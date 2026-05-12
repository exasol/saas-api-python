from __future__ import annotations

import getpass
import logging
import time
from collections.abc import Iterable
from contextlib import contextmanager
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Any,
    TypeVar,
    cast,
)

import tenacity
from tenacity import (
    RetryError,
    TryAgain,
    retry,
)
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_delay
from tenacity.wait import (
    wait_exponential,
    wait_fixed,
)

from exasol.saas.client import Limits
from exasol.saas.client.openapi_facade import (
    AllowedIP,
    ApiError,
    AuthenticatedClient,
    Cluster,
    ClusterConnection,
    ExasolDatabase,
    Status,
)
from exasol.saas.client.openapi_facade import OpenApiFacade as OpenApiClient

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)


def interval_retry(interval: timedelta, timeout: timedelta):
    return tenacity.retry(wait=wait_fixed(interval), stop=stop_after_delay(timeout))


def timestamp_name(project_short_tag: str | None = None) -> str:
    """
    Generates a semi-unique name for a database with the following format:
    - 0-4: number of minutes since the start of the year in hex,
    - 0-5: a semi-random number,
    - provided tag,
    - -username.

    Args:
        project_short_tag: Abbreviation of your project
    """
    now = datetime.now()
    year_start = datetime(now.year, 1, 1)
    minutes_elapsed = int((now - year_start).total_seconds() // 60)
    random_suffix = time.time_ns() % 1048576
    timestamp = f"{minutes_elapsed:05x}{random_suffix:05x}"

    owner = getpass.getuser()
    candidate = f"{timestamp}{project_short_tag or ''}-{owner}"
    return candidate[: Limits.MAX_DATABASE_NAME_LENGTH]


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


class DatabaseDeleteError(Exception):
    """
    Failed to delete a SaaS database instance.
    """


class OpenApiError(Exception):
    def __init__(self, message: str, error: ApiError | None):
        super().__init__(f"{message}: {error.message}." if error else message)


T = TypeVar("T")


def ensure_type(
    expected: type[T],
    response: T | ApiError | None,
    message: str,
) -> T:
    """
    Ensure the passed response is of the expected type and return it with
    correct type. Otherwise raise an OpenApiError.
    """
    if isinstance(response, expected):
        return cast(T, response)
    api_error = response if isinstance(response, ApiError) else None
    raise OpenApiError(message, api_error)


class InternalError(Exception):
    """
    Internal error during delete with retry.
    """


def create_saas_client(
    host: str,
    pat: str,
    raise_on_unexpected_status: bool = True,
) -> AuthenticatedClient:
    return OpenApiClient(
        host=host,
        pat=pat,
        raise_on_unexpected_status=raise_on_unexpected_status,
    )


def _get_database_id(
    account_id: str,
    client: AuthenticatedClient,
    database_name: str,
) -> str:
    """
    Finds the database id, given the database name.
    """
    return client.find_database_id(account_id, database_name)


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
        clusters = ensure_type(
            list,
            client.list_clusters(account_id, database_id),
            "Failed to list clusters of "
            f"host {host}, account {account_id}, database {database_id}",
        )
        cluster_id = next(
            filter(lambda cl: cl.main_cluster, clusters)  # type: ignore
        ).id
        resp = client.get_cluster_connection(account_id, database_id, cluster_id)
        connection = ensure_type(
            ClusterConnection,
            resp,
            "Failed to get the connection data to"
            f" host {host}, account {account_id},"
            f" database with ID {database_id} named {database_name}",
        )
        return {
            "dsn": f"{connection.dns}:{connection.port}",
            "user": connection.db_username,
            "password": pat,
        }


class OpenApiAccess:
    """
    This class is meant to be used only in the context of the API
    generator repository while integration tests in other repositories are
    planned to only use fixture ``saas_database_id()``.
    """

    def __init__(self, client: AuthenticatedClient, account_id: str):
        self._client = client
        self._account_id = account_id

    def create_database(
        self,
        name: str,
        cluster_size: str = "XS",
        region: str = "eu-central-1",
        idle_time: timedelta | None = None,
    ) -> ExasolDatabase | None:
        idle_time = idle_time or Limits.AUTOSTOP_MIN_IDLE_TIME
        LOG.info("Creating database %s", name)
        resp = self._client.create_database(
            self._account_id,
            name=name,
            cluster_size=cluster_size,
            region=region,
            idle_time=idle_time,
        )
        database = ensure_type(
            ExasolDatabase, resp, f"Failed to create database {name}"
        )
        LOG.info("Created database with ID %s", database.id)
        return database

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
        def verify_not_listed() -> bool:
            if database_id in self.list_database_ids():
                raise TryAgain
            return True

        try:
            return verify_not_listed()
        except (TryAgain, RetryError) as ex:
            raise DatabaseDeleteTimeout from ex

    def delete_database(
        self,
        database_id: str,
        ignore_failures: bool = False,
        timeout: timedelta = timedelta(minutes=30),
        min_interval: timedelta = timedelta(seconds=1),
        max_interval: timedelta = timedelta(minutes=2),
    ) -> None:
        def is_retry(resp: ApiError) -> bool:
            return (
                resp.status == 400
                and "cluster is not in a proper state" in resp.message
            )

        @retry(
            wait=wait_exponential(
                multiplier=1,
                min=min_interval,
                max=max_interval,
            ),
            stop=stop_after_delay(timeout),
            retry=retry_if_exception_type(TryAgain),
        )
        def delete_with_retry() -> None:
            LOG.info("- Trying to delete ...")
            resp = self._client.delete_database(
                self._account_id,
                database_id,
            )
            if not isinstance(resp, ApiError):
                # success
                return
            if is_retry(resp):
                raise TryAgain
            raise InternalError(f"HTTP {resp.status}: {resp.message}.")

        LOG.info("Got request to delete database with ID %s", database_id)
        try:
            delete_with_retry()
            LOG.info("Successfully deleted database.")
        except Exception as ex:
            if ignore_failures:
                LOG.warning("Ignoring delete failure: %s", ex)
            else:
                msg = f"Failed to delete database: {ex}"
                LOG.error(msg)
                raise DatabaseDeleteError(msg) from ex

    def list_database_ids(self) -> Iterable[str]:
        resp = self._client.list_databases(self._account_id) or []
        # actually list[ExasolDatabase]
        dbs = ensure_type(list, resp, "Failed to list databases")
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
                self.delete_database(db.id, ignore_delete_failure)
                LOG.info("Context assumes database %s as deleted.", db_repr)

    def get_database(
        self,
        database_id: str,
    ) -> ExasolDatabase | None:
        resp = self._client.get_database(self._account_id, database_id)
        return ensure_type(
            ExasolDatabase, resp, f"Failed to get database {database_id}"
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

        LOG.info("Waiting for database with ID %s to be available:", database_id)
        if poll_status() not in success:
            raise DatabaseStartupFailure()

    def clusters(
        self,
        database_id: str,
    ) -> list[Cluster] | None:
        resp = self._client.list_clusters(self._account_id, database_id) or []
        # actually list[Cluster]
        return ensure_type(
            list, resp, f"Failed to list clusters of database {database_id}"
        )

    def get_connection(
        self,
        database_id: str,
        cluster_id: str,
    ) -> ClusterConnection | None:
        resp = self._client.get_cluster_connection(
            self._account_id, database_id, cluster_id
        )
        return ensure_type(
            ClusterConnection,
            resp,
            "Failed to retrieve a connection to "
            f"database {database_id} cluster {cluster_id}",
        )

    def list_allowed_ip_ids(self) -> Iterable[str]:
        resp = self._client.list_allowed_ips(self._account_id) or []
        # actually list[AllowedIP]
        ips = ensure_type(list, resp, "Failed to retrieve the list of allowed ips")
        return (x.id for x in ips)

    def add_allowed_ip(
        self,
        cidr_ip: str = "0.0.0.0/0",
    ) -> AllowedIP | None:
        """
        Suggested values for cidr_ip:
        * 185.17.207.78/32
        * 0.0.0.0/0 = all ipv4
        * ::/0 = all ipv6
        """
        resp = self._client.add_allowed_ip(
            self._account_id,
            cidr_ip=cidr_ip,
            name=timestamp_name(),
        )
        return ensure_type(
            AllowedIP,
            resp,
            f"Failed to add allowed IP address {cidr_ip}",
        )

    def delete_allowed_ip(self, id: str, ignore_failures=False) -> Any | None:
        with self._ignore_failures(ignore_failures) as client:
            return client.delete_allowed_ip(self._account_id, id)

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
