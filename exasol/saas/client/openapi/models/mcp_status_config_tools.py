from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="McpStatusConfigTools")


@_attrs_define
class McpStatusConfigTools:
    """
    Attributes:
        read (list[str]):
        write (list[str]):
    """

    read: list[str]
    write: list[str]

    def to_dict(self) -> dict[str, Any]:
        read = self.read

        write = self.write

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "read": read,
                "write": write,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = cast(list[str], d.pop("read"))

        write = cast(list[str], d.pop("write"))

        mcp_status_config_tools = cls(
            read=read,
            write=write,
        )

        return mcp_status_config_tools
