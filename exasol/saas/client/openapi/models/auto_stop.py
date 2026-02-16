from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="AutoStop")


@_attrs_define
class AutoStop:
    """
    Attributes:
        enabled (bool):
        idle_time (int):
    """

    enabled: bool
    idle_time: int

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        idle_time = self.idle_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "idleTime": idle_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        idle_time = d.pop("idleTime")

        auto_stop = cls(
            enabled=enabled,
            idle_time=idle_time,
        )

        return auto_stop
