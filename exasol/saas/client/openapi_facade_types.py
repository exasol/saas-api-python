from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any


class Status(str, Enum):
    CREATING = "creating"
    DELETED = "deleted"
    DELETING = "deleting"
    ERROR = "error"
    MAINTENANCE = "maintenance"
    RUNNING = "running"
    SCALING = "scaling"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"
    TOCREATE = "tocreate"
    TODELETE = "todelete"
    TOSCALE = "toscale"
    TOSTART = "tostart"
    TOSTOP = "tostop"

    def __str__(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class ApiError:
    status: float
    message: str
    request_id: str
    path: str
    method: str
    log_id: str
    handler: str
    timestamp: str
    causes: Any | None = None


@dataclass(frozen=True)
class ExasolDatabaseClusters:
    total: int
    running: int


@dataclass(frozen=True)
class ExasolDatabase:
    status: Status
    id: str
    name: str
    clusters: ExasolDatabaseClusters
    provider: str
    region: str
    created_at: datetime
    created_by: str
    integrations: list[Any] | None = None
    deleted_by: str | None = None
    deleted_at: datetime | None = None


@dataclass(frozen=True)
class ClusterSettings:
    offload_enabled: bool
    offload_timeout_min: int


@dataclass(frozen=True)
class AutoStop:
    enabled: bool
    idle_time: int


@dataclass(frozen=True)
class Cluster:
    status: Status
    id: str
    name: str
    size: str
    family_name: str
    created_at: datetime
    created_by: str
    main_cluster: bool
    settings: ClusterSettings
    deleted_at: datetime | None = None
    deleted_by: str | None = None
    auto_stop: AutoStop | None = None


@dataclass(frozen=True)
class ConnectionIPs:
    private: list[str]
    public: list[str]


@dataclass(frozen=True)
class ClusterConnection:
    dns: str
    port: int
    jdbc: str
    ips: ConnectionIPs
    db_username: str


@dataclass(frozen=True)
class AllowedIP:
    id: str
    name: str
    cidr_ip: str
    created_at: datetime
    created_by: str
    deleted_by: str | None = None
    deleted_at: datetime | None = None


__all__ = (
    "AllowedIP",
    "ApiError",
    "AutoStop",
    "Cluster",
    "ClusterConnection",
    "ClusterSettings",
    "ConnectionIPs",
    "ExasolDatabase",
    "ExasolDatabaseClusters",
    "Status",
)
