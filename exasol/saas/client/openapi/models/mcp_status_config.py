from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.mcp_status_config_tools import McpStatusConfigTools


T = TypeVar("T", bound="McpStatusConfig")


@_attrs_define
class McpStatusConfig:
    """
    Attributes:
        tools (McpStatusConfigTools):
        writes_enabled (bool):
    """

    tools: McpStatusConfigTools
    writes_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        tools = self.tools.to_dict()

        writes_enabled = self.writes_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tools": tools,
                "writesEnabled": writes_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_status_config_tools import McpStatusConfigTools

        d = dict(src_dict)
        tools = McpStatusConfigTools.from_dict(d.pop("tools"))

        writes_enabled = d.pop("writesEnabled")

        mcp_status_config = cls(
            tools=tools,
            writes_enabled=writes_enabled,
        )

        return mcp_status_config
