from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.mcp_status_status import McpStatusStatus
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.mcp_status_config import McpStatusConfig


T = TypeVar("T", bound="McpStatus")


@_attrs_define
class McpStatus:
    """
    Attributes:
        status (McpStatusStatus):
        execution_arn (str | Unset):
        last_modified_at (str | Unset):
        connection (str | Unset): MCP server connection string in the form 'https://mcp-<mainClusterDns>:8443/mcp'. The
            endpoint is HTTPS-only and listens on port 8443. Present only when the MCP server is enabled.
        config (McpStatusConfig | Unset):
    """

    status: McpStatusStatus
    execution_arn: str | Unset = UNSET
    last_modified_at: str | Unset = UNSET
    connection: str | Unset = UNSET
    config: McpStatusConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        execution_arn = self.execution_arn

        last_modified_at = self.last_modified_at

        connection = self.connection

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if execution_arn is not UNSET:
            field_dict["executionArn"] = execution_arn
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if connection is not UNSET:
            field_dict["connection"] = connection
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_status_config import McpStatusConfig

        d = dict(src_dict)
        status = McpStatusStatus(d.pop("status"))

        execution_arn = d.pop("executionArn", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        connection = d.pop("connection", UNSET)

        _config = d.pop("config", UNSET)
        config: McpStatusConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = McpStatusConfig.from_dict(_config)

        mcp_status = cls(
            status=status,
            execution_arn=execution_arn,
            last_modified_at=last_modified_at,
            connection=connection,
            config=config,
        )

        return mcp_status
