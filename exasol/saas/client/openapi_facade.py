from __future__ import annotations

from datetime import timedelta
from typing import (
    Any,
    Callable,
    TypeAlias,
    TypeVar,
)

from exasol.saas.client import openapi
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
from exasol.saas.client.openapi.models import (
    AllowedIP as GeneratedAllowedIP,
)
from exasol.saas.client.openapi.models import (
    ApiError as GeneratedApiError,
)
from exasol.saas.client.openapi.models import (
    AutoStop as GeneratedAutoStop,
)
from exasol.saas.client.openapi.models import (
    Cluster as GeneratedCluster,
)
from exasol.saas.client.openapi.models import (
    ClusterConnection as GeneratedClusterConnection,
)
from exasol.saas.client.openapi.models import (
    ClusterSettings as GeneratedClusterSettings,
)
from exasol.saas.client.openapi.models import (
    ConnectionIPs as GeneratedConnectionIPs,
)
from exasol.saas.client.openapi.models import (
    CreateAllowedIP,
    CreateDatabase,
    CreateDatabaseInitialCluster,
)
from exasol.saas.client.openapi.models import (
    ExasolDatabase as GeneratedExasolDatabase,
)
from exasol.saas.client.openapi.models import (
    ExasolDatabaseClusters as GeneratedExasolDatabaseClusters,
)
from exasol.saas.client.openapi.types import UNSET
from exasol.saas.client.openapi_facade_types import (
    AllowedIP,
    ApiError,
    AutoStop,
    Cluster,
    ClusterConnection,
    ClusterSettings,
    ConnectionIPs,
    ExasolDatabase,
    ExasolDatabaseClusters,
    Status,
)


def _minutes(duration: timedelta) -> int:
    return duration.seconds // 60


def _optional(value: Any) -> Any | None:
    return None if value is UNSET else value


def _convert_status(value: Any) -> Status:
    return Status(str(value))


def _convert_api_error(error: GeneratedApiError) -> ApiError:
    return ApiError(
        status=error.status,
        message=error.message,
        request_id=error.request_id,
        path=error.path,
        method=error.method,
        log_id=error.log_id,
        handler=error.handler,
        timestamp=error.timestamp,
        causes=_optional(error.causes),
    )


def _convert_database_clusters(
    clusters: GeneratedExasolDatabaseClusters,
) -> ExasolDatabaseClusters:
    return ExasolDatabaseClusters(
        total=clusters.total,
        running=clusters.running,
    )


def _convert_database(database: GeneratedExasolDatabase) -> ExasolDatabase:
    integrations = _optional(database.integrations)
    return ExasolDatabase(
        status=_convert_status(database.status),
        id=database.id,
        name=database.name,
        clusters=_convert_database_clusters(database.clusters),
        provider=database.provider,
        region=database.region,
        created_at=database.created_at,
        created_by=database.created_by,
        integrations=integrations,
        deleted_by=_optional(database.deleted_by),
        deleted_at=_optional(database.deleted_at),
    )


def _convert_cluster_settings(settings: GeneratedClusterSettings) -> ClusterSettings:
    return ClusterSettings(
        offload_enabled=settings.offload_enabled,
        offload_timeout_min=settings.offload_timeout_min,
    )


def _convert_auto_stop(auto_stop: GeneratedAutoStop) -> AutoStop:
    return AutoStop(
        enabled=auto_stop.enabled,
        idle_time=auto_stop.idle_time,
    )


def _convert_cluster(cluster: GeneratedCluster) -> Cluster:
    auto_stop = _optional(cluster.auto_stop)
    return Cluster(
        status=_convert_status(cluster.status),
        id=cluster.id,
        name=cluster.name,
        size=cluster.size,
        family_name=cluster.family_name,
        created_at=cluster.created_at,
        created_by=cluster.created_by,
        main_cluster=cluster.main_cluster,
        settings=_convert_cluster_settings(cluster.settings),
        deleted_at=_optional(cluster.deleted_at),
        deleted_by=_optional(cluster.deleted_by),
        auto_stop=_convert_auto_stop(auto_stop) if auto_stop else None,
    )


def _convert_connection_ips(ips: GeneratedConnectionIPs) -> ConnectionIPs:
    return ConnectionIPs(private=ips.private, public=ips.public)


def _convert_cluster_connection(
    connection: GeneratedClusterConnection,
) -> ClusterConnection:
    return ClusterConnection(
        dns=connection.dns,
        port=connection.port,
        jdbc=connection.jdbc,
        ips=_convert_connection_ips(connection.ips),
        db_username=connection.db_username,
    )


def _convert_allowed_ip(allowed_ip: GeneratedAllowedIP) -> AllowedIP:
    return AllowedIP(
        id=allowed_ip.id,
        name=allowed_ip.name,
        cidr_ip=allowed_ip.cidr_ip,
        created_at=allowed_ip.created_at,
        created_by=allowed_ip.created_by,
        deleted_by=_optional(allowed_ip.deleted_by),
        deleted_at=_optional(allowed_ip.deleted_at),
    )


TGenerated = TypeVar("TGenerated")
TConverted = TypeVar("TConverted")


def _map_result(
    result: TGenerated | GeneratedApiError | None,
    converter: Callable[[TGenerated], TConverted],
) -> TConverted | ApiError | None:
    if result is None:
        return None
    if isinstance(result, GeneratedApiError):
        return _convert_api_error(result)
    return converter(result)


class OpenApiFacade:
    def __init__(
        self,
        host: str,
        pat: str,
        raise_on_unexpected_status: bool = True,
    ):
        self._client = openapi.AuthenticatedClient(
            base_url=host,
            token=pat,
            raise_on_unexpected_status=raise_on_unexpected_status,
        )

    @property
    def raise_on_unexpected_status(self) -> bool:
        return self._client.raise_on_unexpected_status

    @raise_on_unexpected_status.setter
    def raise_on_unexpected_status(self, value: bool) -> None:
        self._client.raise_on_unexpected_status = value

    def __enter__(self) -> OpenApiFacade:
        self._client.__enter__()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self._client.__exit__(*args, **kwargs)

    def list_databases(
        self, account_id: str
    ) -> list[ExasolDatabase] | ApiError | None:
        result = list_databases.sync(account_id, client=self._client)
        if isinstance(result, list):
            return [_convert_database(item) for item in result]
        return _map_result(result, _convert_database)

    def find_database_id(self, account_id: str, database_name: str) -> str:
        databases = self.list_databases(account_id)
        if not isinstance(databases, list):
            raise RuntimeError(f"SaaS database {database_name} was not found.")

        matches = [
            db
            for db in databases
            if db.name == database_name
            and db.deleted_at is None
            and db.deleted_by is None
        ]
        if not matches:
            raise RuntimeError(f"SaaS database {database_name} was not found.")
        return matches[0].id

    def create_database(
        self,
        account_id: str,
        name: str,
        cluster_size: str,
        region: str,
        idle_time: timedelta,
    ) -> ExasolDatabase | ApiError | None:
        cluster_spec = CreateDatabaseInitialCluster(
            name="my-cluster",
            size=cluster_size,
            auto_stop=GeneratedAutoStop(
                enabled=True,
                idle_time=_minutes(idle_time),
            ),
        )
        body = CreateDatabase(
            name=name,
            initial_cluster=cluster_spec,
            provider="aws",
            region=region,
            stream_type="innovation-release",
        )
        result = create_database.sync(
            account_id,
            client=self._client,
            body=body,
        )
        return _map_result(result, _convert_database)

    def get_database(
        self, account_id: str, database_id: str
    ) -> ExasolDatabase | ApiError | None:
        result = get_database.sync(account_id, database_id, client=self._client)
        return _map_result(result, _convert_database)

    def delete_database(
        self, account_id: str, database_id: str
    ) -> Any | ApiError | None:
        result = delete_database.sync(account_id, database_id, client=self._client)
        if isinstance(result, GeneratedApiError):
            return _convert_api_error(result)
        return result

    def list_clusters(
        self, account_id: str, database_id: str
    ) -> list[Cluster] | ApiError | None:
        result = list_clusters.sync(account_id, database_id, client=self._client)
        if isinstance(result, list):
            return [_convert_cluster(item) for item in result]
        return _map_result(result, _convert_cluster)

    def get_cluster_connection(
        self, account_id: str, database_id: str, cluster_id: str
    ) -> ClusterConnection | ApiError | None:
        result = get_cluster_connection.sync(
            account_id, database_id, cluster_id, client=self._client
        )
        return _map_result(result, _convert_cluster_connection)

    def list_allowed_ips(
        self, account_id: str
    ) -> list[AllowedIP] | ApiError | None:
        result = list_allowed_i_ps.sync(account_id, client=self._client)
        if isinstance(result, list):
            return [_convert_allowed_ip(item) for item in result]
        return _map_result(result, _convert_allowed_ip)

    def add_allowed_ip(
        self,
        account_id: str,
        cidr_ip: str,
        name: str,
    ) -> AllowedIP | ApiError | None:
        rule = CreateAllowedIP(name=name, cidr_ip=cidr_ip)
        result = add_allowed_ip.sync(
            account_id,
            client=self._client,
            body=rule,
        )
        return _map_result(result, _convert_allowed_ip)

    def delete_allowed_ip(
        self, account_id: str, allowed_ip_id: str
    ) -> Any | ApiError | None:
        result = delete_allowed_ip.sync(
            account_id,
            allowed_ip_id,
            client=self._client,
        )
        if isinstance(result, GeneratedApiError):
            return _convert_api_error(result)
        return result


AuthenticatedClient: TypeAlias = OpenApiFacade

__all__ = (
    "AllowedIP",
    "ApiError",
    "AuthenticatedClient",
    "AutoStop",
    "Cluster",
    "ClusterConnection",
    "ClusterSettings",
    "ConnectionIPs",
    "ExasolDatabase",
    "ExasolDatabaseClusters",
    "OpenApiFacade",
    "Status",
)
