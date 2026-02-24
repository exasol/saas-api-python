from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClusterActionScale")


@_attrs_define
class ClusterActionScale:
    """
    Attributes:
        cluster_id (str):
        size (str):
    """

    cluster_id: str
    size: str

    def to_dict(self) -> dict[str, Any]:
        cluster_id = self.cluster_id

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "clusterId": cluster_id,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_id = d.pop("clusterId")

        size = d.pop("size")

        cluster_action_scale = cls(
            cluster_id=cluster_id,
            size=size,
        )

        return cluster_action_scale
