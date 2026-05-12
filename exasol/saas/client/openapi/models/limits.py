from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Limits")


@_attrs_define
class Limits:
    """
    Attributes:
        worker_clusters (int):
        databases (int):
        cluster_sizes (list[str]):
    """

    worker_clusters: int
    databases: int
    cluster_sizes: list[str]

    def to_dict(self) -> dict[str, Any]:
        worker_clusters = self.worker_clusters

        databases = self.databases

        cluster_sizes = self.cluster_sizes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workerClusters": worker_clusters,
                "databases": databases,
                "clusterSizes": cluster_sizes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        worker_clusters = d.pop("workerClusters")

        databases = d.pop("databases")

        cluster_sizes = cast(list[str], d.pop("clusterSizes"))

        limits = cls(
            worker_clusters=worker_clusters,
            databases=databases,
            cluster_sizes=cluster_sizes,
        )

        return limits
