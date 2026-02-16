from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetAutoUpdatesDatabase")


@_attrs_define
class SetAutoUpdatesDatabase:
    """
    Attributes:
        auto_updates_enabled (bool):
    """

    auto_updates_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        auto_updates_enabled = self.auto_updates_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "autoUpdatesEnabled": auto_updates_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_updates_enabled = d.pop("autoUpdatesEnabled")

        set_auto_updates_database = cls(
            auto_updates_enabled=auto_updates_enabled,
        )

        return set_auto_updates_database
