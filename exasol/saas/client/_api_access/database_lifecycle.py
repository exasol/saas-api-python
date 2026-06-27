from __future__ import annotations

from collections.abc import (
    Callable,
    Iterable,
)
from datetime import timedelta

from tenacity import (
    RetryError,
    TryAgain,
    retry,
)
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_delay
from tenacity.wait import wait_exponential

from exasol.saas.client import (
    Limits,
    openapi,
)
from exasol.saas.client._api_access.common import (
    LOG,
    _is_not_found,
    _log_api_output,
    ensure_type,
    interval_retry,
)
from exasol.saas.client._api_access.errors import (
    DatabaseDeleteTimeout,
    DatabaseStartupFailure,
    InternalError,
    OpenApiError,
)
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    get_database,
    get_database_settings,
    list_databases,
)
from exasol.saas.client.openapi.models import (
    ApiError,
    ExasolDatabase,
    Status,
)
from exasol.saas.client.openapi.types import UNSET


def _minutes(value: timedelta) -> int:
    return value.seconds // 60


def _build_database_spec(
    name: str,
    cluster_size: str,
    region: str,
    idle_time: timedelta | None,
    num_nodes: int | None,
) -> openapi.models.CreateDatabase:
    idle_time = idle_time or Limits.AUTOSTOP_MIN_IDLE_TIME
    cluster_spec = openapi.models.CreateDatabaseInitialCluster(
        name="my-cluster",
        size=cluster_size,
        auto_stop=openapi.models.AutoStop(
            enabled=True,
            idle_time=_minutes(idle_time),
        ),
    )
    database_spec = openapi.models.CreateDatabase(
        name=name,
        initial_cluster=cluster_spec,
        provider="aws",
        region=region,
        stream_type="innovation-release",
    )
    if num_nodes is not None:
        database_spec.num_nodes = num_nodes
    return database_spec


def _create_database(
    account_id: str,
    client: openapi.AuthenticatedClient,
    name: str,
    cluster_size: str,
    region: str,
    idle_time: timedelta | None,
    num_nodes: int | None,
) -> ExasolDatabase:
    LOG.info("Creating database %s", name)
    resp = create_database.sync(
        account_id,
        client=client,
        body=_build_database_spec(
            name=name,
            cluster_size=cluster_size,
            region=region,
            idle_time=idle_time,
            num_nodes=num_nodes,
        ),
    )
    _log_api_output(
        "create_database.sync",
        resp,
        account_id=account_id,
        database_name=name,
    )
    database = ensure_type(ExasolDatabase, resp, f"Failed to create database {name}")
    LOG.info("Created database with ID %s", database.id)
    return database


def _list_active_database_ids(
    account_id: str,
    client: openapi.AuthenticatedClient,
) -> list[str]:
    resp = list_databases.sync(account_id, client=client) or []
    _log_api_output(
        "list_databases.sync",
        resp,
        account_id=account_id,
    )
    dbs = ensure_type(list, resp, "Failed to list databases")
    active_database_ids = [
        db.id
        for db in dbs
        if db.deleted_at is UNSET
        and db.deleted_by is UNSET
        and db.status not in {Status.DELETING, Status.TODELETE}
    ]
    LOG.debug("list_database_ids visible IDs: %s", active_database_ids)
    return active_database_ids


def _wait_until_database_deleted(
    account_id: str,
    client: openapi.AuthenticatedClient,
    database_id: str,
    list_database_ids: Callable[[], Iterable[str]],
    timeout: timedelta,
    interval: timedelta,
) -> None:
    terminal = {Status.DELETED}
    in_progress = {Status.DELETING, Status.TODELETE}

    @interval_retry(interval, timeout)
    def verify_deleted() -> bool:
        resp = get_database.sync(
            account_id,
            database_id,
            client=client,
        )
        _log_api_output(
            "get_database.sync",
            resp,
            account_id=account_id,
            database_id=database_id,
        )
        if isinstance(resp, ApiError):
            if _is_not_found(resp):
                return True
            raise OpenApiError(
                f"Failed to get database {database_id}",
                resp,
            )

        if resp is None:
            LOG.info("- Database deletion status: unavailable ...")
            raise TryAgain

        if resp.deleted_at is not UNSET or resp.deleted_by is not UNSET:
            return True

        if resp.status in terminal:
            return True

        visible_database_ids = list(list_database_ids())
        LOG.debug(
            "wait_until_deleted visible database IDs {'database_id': %s}: %s",
            database_id,
            visible_database_ids,
        )
        if database_id not in visible_database_ids:
            return True

        if resp.status in in_progress:
            LOG.info("- Database deletion status: %s ...", resp.status)
            raise TryAgain

        if database_id in visible_database_ids:
            LOG.info("- Database deletion status: %s ...", resp.status)
            raise TryAgain

        return True

    try:
        verify_deleted()
    except (TryAgain, RetryError) as ex:
        raise DatabaseDeleteTimeout from ex


def _is_database_delete_retry(resp: ApiError) -> bool:
    return resp.status == 400 and "cluster is not in a proper state" in resp.message


def _delete_database_with_retry(
    account_id: str,
    client: openapi.AuthenticatedClient,
    database_id: str,
    timeout: timedelta,
    min_interval: timedelta,
    max_interval: timedelta,
) -> None:
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
        resp = delete_database.sync(
            account_id,
            database_id,
            client=client,
        )
        _log_api_output(
            "delete_database.sync",
            resp,
            account_id=account_id,
            database_id=database_id,
        )
        if not isinstance(resp, ApiError):
            return
        if _is_database_delete_retry(resp):
            raise TryAgain
        raise InternalError(f"HTTP {resp.status}: {resp.message}.")

    delete_with_retry()


def _retrieve_database_settings(
    account_id: str,
    client: openapi.AuthenticatedClient,
    database_id: str,
) -> openapi.models.DatabaseSettings:
    @interval_retry(
        interval=timedelta(seconds=5),
        timeout=timedelta(minutes=2),
    )
    def retrieve_settings() -> openapi.models.DatabaseSettings:
        resp = get_database_settings.sync(
            account_id,
            database_id,
            client=client,
        )
        _log_api_output(
            "get_database_settings.sync",
            resp,
            account_id=account_id,
            database_id=database_id,
        )
        if isinstance(resp, ApiError) and _is_not_found(resp):
            raise TryAgain
        return ensure_type(
            openapi.models.DatabaseSettings,
            resp,
            f"Failed to get settings of database {database_id}",
        )

    return retrieve_settings()


def _wait_until_database_running(
    database_id: str,
    get_database_by_id: Callable[[str], ExasolDatabase | None],
    timeout: timedelta,
    interval: timedelta,
) -> None:
    success = [Status.RUNNING]

    @interval_retry(interval, timeout)
    def poll_status() -> Status:
        db = get_database_by_id(database_id)
        status = db.status if db else None
        if status not in success:
            LOG.info("- Database status: %s ...", status)
            raise TryAgain
        return status

    LOG.info("Waiting for database with ID %s to be available:", database_id)
    if poll_status() not in success:
        raise DatabaseStartupFailure()
