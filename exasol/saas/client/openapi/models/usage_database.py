from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.usage_cluster import UsageCluster


T = TypeVar("T", bound="UsageDatabase")


@_attrs_define
class UsageDatabase:
    """
    Attributes:
        id (str):
        name (str):
        clusters (list[UsageCluster]):
        region (str | Unset): Region the database runs in. Absent when unknown, and while usage is served by the legacy
            usage service (rollback mode), which does not return it.
        used_storage (float | Unset):
        storage_credits (float | Unset): Credits of the database's storage that day: its GB-month share of the day × the
            per-GB-month storage price, computed the way the invoice's storage line is. Credits are the unit of
            /billing/credits (saas.prices.price_per_unit), computed at the price the usage was attributed at, the price in
            force on the usage's day. Present whenever usedStorage is present, 0 when the product is free, absent when the
            price could not be resolved. Absent while usage is served by the legacy usage service (rollback mode), which
            does not return it.
    """

    id: str
    name: str
    clusters: list[UsageCluster]
    region: str | Unset = UNSET
    used_storage: float | Unset = UNSET
    storage_credits: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        clusters = []
        for clusters_item_data in self.clusters:
            clusters_item = clusters_item_data.to_dict()
            clusters.append(clusters_item)

        region = self.region

        used_storage = self.used_storage

        storage_credits = self.storage_credits

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "clusters": clusters,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if used_storage is not UNSET:
            field_dict["usedStorage"] = used_storage
        if storage_credits is not UNSET:
            field_dict["storageCredits"] = storage_credits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_cluster import UsageCluster

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        clusters = []
        _clusters = d.pop("clusters")
        for clusters_item_data in _clusters:
            clusters_item = UsageCluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        region = d.pop("region", UNSET)

        used_storage = d.pop("usedStorage", UNSET)

        storage_credits = d.pop("storageCredits", UNSET)

        usage_database = cls(
            id=id,
            name=name,
            clusters=clusters,
            region=region,
            used_storage=used_storage,
            storage_credits=storage_credits,
        )

        return usage_database
