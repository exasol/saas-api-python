from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.toggle_mcp_action_action import ToggleMcpActionAction

T = TypeVar("T", bound="ToggleMcpAction")


@_attrs_define
class ToggleMcpAction:
    """
    Attributes:
        action (ToggleMcpActionAction):
    """

    action: ToggleMcpActionAction

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ToggleMcpActionAction(d.pop("action"))

        toggle_mcp_action = cls(
            action=action,
        )

        return toggle_mcp_action
