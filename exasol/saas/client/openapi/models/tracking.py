from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Tracking")


@_attrs_define
class Tracking:
    """
    Attributes:
        enabled (bool):
        api_key (str):
    """

    enabled: bool
    api_key: str

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        api_key = self.api_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        api_key = d.pop("apiKey")

        tracking = cls(
            enabled=enabled,
            api_key=api_key,
        )

        return tracking
