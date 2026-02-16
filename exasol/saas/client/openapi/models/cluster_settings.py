from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClusterSettings")


@_attrs_define
class ClusterSettings:
    """
    Attributes:
        offload_enabled (bool):
        offload_timeout_min (int):
    """

    offload_enabled: bool
    offload_timeout_min: int

    def to_dict(self) -> dict[str, Any]:
        offload_enabled = self.offload_enabled

        offload_timeout_min = self.offload_timeout_min

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offloadEnabled": offload_enabled,
                "offloadTimeoutMin": offload_timeout_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offload_enabled = d.pop("offloadEnabled")

        offload_timeout_min = d.pop("offloadTimeoutMin")

        cluster_settings = cls(
            offload_enabled=offload_enabled,
            offload_timeout_min=offload_timeout_min,
        )

        return cluster_settings
