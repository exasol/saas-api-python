from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="ClusterSettingsUpdate")


@_attrs_define
class ClusterSettingsUpdate:
    """
    Attributes:
        offload_enabled (bool | Unset):
        offload_timeout_min (int | Unset):
    """

    offload_enabled: bool | Unset = UNSET
    offload_timeout_min: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offload_enabled = self.offload_enabled

        offload_timeout_min = self.offload_timeout_min

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if offload_enabled is not UNSET:
            field_dict["offloadEnabled"] = offload_enabled
        if offload_timeout_min is not UNSET:
            field_dict["offloadTimeoutMin"] = offload_timeout_min

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offload_enabled = d.pop("offloadEnabled", UNSET)

        offload_timeout_min = d.pop("offloadTimeoutMin", UNSET)

        cluster_settings_update = cls(
            offload_enabled=offload_enabled,
            offload_timeout_min=offload_timeout_min,
        )

        return cluster_settings_update
