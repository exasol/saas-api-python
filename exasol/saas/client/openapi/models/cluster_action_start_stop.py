from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClusterActionStartStop")


@_attrs_define
class ClusterActionStartStop:
    """
    Attributes:
        cluster_id (str):
    """

    cluster_id: str

    def to_dict(self) -> dict[str, Any]:
        cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "clusterId": cluster_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_id = d.pop("clusterId")

        cluster_action_start_stop = cls(
            cluster_id=cluster_id,
        )

        return cluster_action_start_stop
