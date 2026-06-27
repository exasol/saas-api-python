from __future__ import annotations

from collections.abc import Iterable
from contextlib import contextmanager
from datetime import timedelta
from typing import Any

from exasol.saas.client import openapi
from exasol.saas.client._api_access.allowed_ip_lifecycle import (
    _add_allowed_ip,
    _list_active_allowed_ip_ids,
    _resolve_active_allowed_ip,
    _wait_until_allowed_ip_deleted,
)
from exasol.saas.client._api_access.common import (
    LOG,
    _log_api_output,
    ensure_type,
)
from exasol.saas.client._api_access.database_lifecycle import (
    _create_database,
    _delete_database_with_retry,
    _list_active_database_ids,
    _retrieve_database_settings,
    _wait_until_database_deleted,
    _wait_until_database_running,
)
from exasol.saas.client._api_access.errors import DatabaseDeleteError
from exasol.saas.client.openapi.api.clusters import (
    get_cluster_connection,
    list_clusters,
)
from exasol.saas.client.openapi.api.databases import get_database
from exasol.saas.client.openapi.api.security import delete_allowed_ip
from exasol.saas.client.openapi.api.security import get_allowed_ip as get_allowed_ip_api
from exasol.saas.client.openapi.models import (
    ApiError,
    ExasolDatabase,
)


class OpenApiAccess:
    """
    This class is meant to be used only in the context of the API
    generator repository while integration tests in other repositories are
    planned to only use fixture ``saas_database_id()``.
    """

    def __init__(self, client: openapi.AuthenticatedClient, account_id: str):
        self._client = client
        self._account_id = account_id

    @contextmanager
    def _ignore_failures(self, ignore: bool = False):
        before = self._client.raise_on_unexpected_status
        self._client.raise_on_unexpected_status = not ignore
        yield self._client
        self._client.raise_on_unexpected_status = before

    def create_database(
        self,
        name: str,
        cluster_size: str = "XS",
        region: str = "eu-central-1",
        idle_time: timedelta | None = None,
        num_nodes: int | None = None,
    ) -> ExasolDatabase | None:
        return _create_database(
            account_id=self._account_id,
            client=self._client,
            name=name,
            cluster_size=cluster_size,
            region=region,
            idle_time=idle_time,
            num_nodes=num_nodes,
        )

    def wait_until_deleted(
        self,
        database_id: str,
        timeout: timedelta = timedelta(minutes=20),
        interval: timedelta = timedelta(seconds=10),
    ):
        return _wait_until_database_deleted(
            account_id=self._account_id,
            client=self._client,
            database_id=database_id,
            list_database_ids=self.list_database_ids,
            timeout=timeout,
            interval=interval,
        )

    def delete_database(
        self,
        database_id: str,
        ignore_failures: bool = False,
        timeout: timedelta = timedelta(minutes=45),
        min_interval: timedelta = timedelta(seconds=1),
        max_interval: timedelta = timedelta(minutes=2),
    ) -> None:
        LOG.info("Got request to delete database with ID %s", database_id)
        try:
            _delete_database_with_retry(
                account_id=self._account_id,
                client=self._client,
                database_id=database_id,
                timeout=timeout,
                min_interval=min_interval,
                max_interval=max_interval,
            )
            LOG.info("Successfully deleted database.")
        except Exception as ex:
            if ignore_failures:
                LOG.warning("Ignoring delete failure: %s", ex)
            else:
                msg = f"Failed to delete database: {ex}"
                LOG.error(msg)
                raise DatabaseDeleteError(msg) from ex

    def list_database_ids(self) -> Iterable[str]:
        return iter(_list_active_database_ids(self._account_id, self._client))

    @contextmanager
    def database(
        self,
        name: str,
        keep: bool = False,
        ignore_delete_failure: bool = False,
        idle_time: timedelta | None = None,
        num_nodes: int | None = None,
    ):
        db = None
        try:
            db = self.create_database(
                name,
                idle_time=idle_time,
                num_nodes=num_nodes,
            )
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
        resp = get_database.sync(
            self._account_id,
            database_id,
            client=self._client,
        )
        _log_api_output(
            "get_database.sync",
            resp,
            account_id=self._account_id,
            database_id=database_id,
        )
        return ensure_type(
            ExasolDatabase, resp, f"Failed to get database {database_id}"
        )

    def get_database_settings(
        self,
        database_id: str,
    ) -> openapi.models.DatabaseSettings | None:
        return _retrieve_database_settings(
            account_id=self._account_id,
            client=self._client,
            database_id=database_id,
        )

    def wait_until_running(
        self,
        database_id: str,
        timeout: timedelta = timedelta(minutes=45),
        interval: timedelta = timedelta(minutes=2),
    ):
        _wait_until_database_running(
            database_id=database_id,
            get_database_by_id=self.get_database,
            timeout=timeout,
            interval=interval,
        )

    def clusters(
        self,
        database_id: str,
    ) -> list[openapi.models.Cluster] | None:
        resp = (
            list_clusters.sync(
                self._account_id,
                database_id,
                client=self._client,
            )
            or []
        )
        _log_api_output(
            "list_clusters.sync",
            resp,
            account_id=self._account_id,
            database_id=database_id,
        )
        return ensure_type(
            list, resp, f"Failed to list clusters of database {database_id}"
        )

    def get_connection(
        self,
        database_id: str,
        cluster_id: str,
    ) -> openapi.models.ClusterConnection | None:
        resp = get_cluster_connection.sync(
            self._account_id,
            database_id,
            cluster_id,
            client=self._client,
        )
        _log_api_output(
            "get_cluster_connection.sync",
            resp,
            account_id=self._account_id,
            database_id=database_id,
            cluster_id=cluster_id,
        )
        return ensure_type(
            openapi.models.ClusterConnection,
            resp,
            "Failed to retrieve a connection to "
            f"database {database_id} cluster {cluster_id}",
        )

    def list_allowed_ip_ids(self) -> Iterable[str]:
        return iter(_list_active_allowed_ip_ids(self._account_id, self._client))

    def get_allowed_ip(
        self,
        allowed_ip_id: str,
    ) -> openapi.models.AllowedIP | ApiError | None:
        resp = get_allowed_ip_api.sync(
            self._account_id,
            allowed_ip_id,
            client=self._client,
        )
        _log_api_output(
            "get_allowed_ip.sync",
            resp,
            account_id=self._account_id,
            allowed_ip_id=allowed_ip_id,
        )
        return resp

    def wait_until_allowed_ip_listed(
        self,
        allowed_ip_id: str,
        timeout: timedelta = timedelta(minutes=6),
        interval: timedelta = timedelta(seconds=5),
    ) -> None:
        _resolve_active_allowed_ip(
            allowed_ip_id=allowed_ip_id,
            get_allowed_ip_by_id=self.get_allowed_ip,
            timeout=timeout,
            interval=interval,
        )

    def wait_until_allowed_ip_deleted(
        self,
        allowed_ip_id: str,
        timeout: timedelta = timedelta(minutes=10),
        interval: timedelta = timedelta(seconds=5),
    ) -> None:
        _wait_until_allowed_ip_deleted(
            allowed_ip_id=allowed_ip_id,
            get_allowed_ip_by_id=self.get_allowed_ip,
            timeout=timeout,
            interval=interval,
        )

    def add_allowed_ip(
        self,
        cidr_ip: str = "0.0.0.0/0",
    ) -> openapi.models.AllowedIP | None:
        """
        Suggested values for cidr_ip:
        * 185.17.207.78/32
        * 0.0.0.0/0 = all ipv4
        * ::/0 = all ipv6
        """
        return _add_allowed_ip(
            account_id=self._account_id,
            client=self._client,
            cidr_ip=cidr_ip,
            get_allowed_ip_by_id=self.get_allowed_ip,
        )

    def delete_allowed_ip(self, id: str, ignore_failures=False) -> Any | None:
        with self._ignore_failures(ignore_failures) as client:
            resp = delete_allowed_ip.sync(self._account_id, id, client=client)
            _log_api_output(
                "delete_allowed_ip.sync",
                resp,
                account_id=self._account_id,
                allowed_ip_id=id,
            )
            return resp

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
