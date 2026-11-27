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

T = TypeVar("T", bound="UsageCluster")


@_attrs_define
class UsageCluster:
    """
    Attributes:
        id (str):
        size (str):
        name (str):
        main_cluster (bool | Unset): true for the main cluster, false for a worker. Absent when unknown, and while usage
            is served by the legacy usage service (rollback mode), which does not return it; absent does not mean worker.
        family (str | Unset): Instance family the cluster ran on, e.g. r5d or r6id. A cluster resized across families
            within a day appears once per (size, family). Absent when unknown, and while usage is served by the legacy usage
            service (rollback mode), which does not return it.
        compute (float | Unset): Wall-clock hours the cluster spent in a billable state that day, independent of its
            size and node count. See computeVcpuHours for the billed figure.
        compute_vcpu_hours (float | Unset): Billed vCPU-hours of the cluster that day: running hours × number of nodes ×
            vCPUs per node, the figure the invoice's compute line is based on. Absent for a day before 2026-07 on which a
            compute row of the cluster was priced without an instance family (the pre-family price): its hours are derived
            with the legacy factor and no vCPU figure is known. Also absent while usage is served by the legacy usage
            service (rollback mode), which does not return it.
        compute_credits (float | Unset): Credits of the cluster's compute that day: computeVcpuHours × the per-vCPU-hour
            price of its instance family and region. Credits are the unit of /billing/credits (saas.prices.price_per_unit),
            computed, for days from 2026-07, with the price current at request time (the compute source carries no price and
            saas.prices keeps no history), and for earlier days at the price the usage was attributed at. Present whenever
            compute is present, 0 when the product is free, absent when the price could not be resolved. Absent while usage
            is served by the legacy usage service (rollback mode), which does not return it.
        out_same_region (float | Unset):
        out_same_region_credits (float | Unset): Credits of outSameRegion that day: GB × the price of the same-region
            traffic sub product (0 while that traffic is free). Credits are the unit of /billing/credits
            (saas.prices.price_per_unit), computed at the price the usage was attributed at, the price in force on the
            usage's day. Present whenever outSameRegion is present, 0 when the product is free, absent when the price could
            not be resolved. Absent while usage is served by the legacy usage service (rollback mode), which does not return
            it.
        out_different_region (float | Unset):
        out_different_region_credits (float | Unset): Credits of outDifferentRegion that day: GB × the price of the
            cross-region traffic sub product. Credits are the unit of /billing/credits (saas.prices.price_per_unit),
            computed at the price the usage was attributed at, the price in force on the usage's day. Present whenever
            outDifferentRegion is present, 0 when the product is free, absent when the price could not be resolved. Absent
            while usage is served by the legacy usage service (rollback mode), which does not return it.
        out_internet (float | Unset):
        out_internet_credits (float | Unset): Credits of outInternet that day: GB × the price of the internet egress sub
            product. Credits are the unit of /billing/credits (saas.prices.price_per_unit), computed at the price the usage
            was attributed at, the price in force on the usage's day. Present whenever outInternet is present, 0 when the
            product is free, absent when the price could not be resolved. Absent while usage is served by the legacy usage
            service (rollback mode), which does not return it.
    """

    id: str
    size: str
    name: str
    main_cluster: bool | Unset = UNSET
    family: str | Unset = UNSET
    compute: float | Unset = UNSET
    compute_vcpu_hours: float | Unset = UNSET
    compute_credits: float | Unset = UNSET
    out_same_region: float | Unset = UNSET
    out_same_region_credits: float | Unset = UNSET
    out_different_region: float | Unset = UNSET
    out_different_region_credits: float | Unset = UNSET
    out_internet: float | Unset = UNSET
    out_internet_credits: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        size = self.size

        name = self.name

        main_cluster = self.main_cluster

        family = self.family

        compute = self.compute

        compute_vcpu_hours = self.compute_vcpu_hours

        compute_credits = self.compute_credits

        out_same_region = self.out_same_region

        out_same_region_credits = self.out_same_region_credits

        out_different_region = self.out_different_region

        out_different_region_credits = self.out_different_region_credits

        out_internet = self.out_internet

        out_internet_credits = self.out_internet_credits

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "size": size,
                "name": name,
            }
        )
        if main_cluster is not UNSET:
            field_dict["mainCluster"] = main_cluster
        if family is not UNSET:
            field_dict["family"] = family
        if compute is not UNSET:
            field_dict["compute"] = compute
        if compute_vcpu_hours is not UNSET:
            field_dict["computeVcpuHours"] = compute_vcpu_hours
        if compute_credits is not UNSET:
            field_dict["computeCredits"] = compute_credits
        if out_same_region is not UNSET:
            field_dict["outSameRegion"] = out_same_region
        if out_same_region_credits is not UNSET:
            field_dict["outSameRegionCredits"] = out_same_region_credits
        if out_different_region is not UNSET:
            field_dict["outDifferentRegion"] = out_different_region
        if out_different_region_credits is not UNSET:
            field_dict["outDifferentRegionCredits"] = out_different_region_credits
        if out_internet is not UNSET:
            field_dict["outInternet"] = out_internet
        if out_internet_credits is not UNSET:
            field_dict["outInternetCredits"] = out_internet_credits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        size = d.pop("size")

        name = d.pop("name")

        main_cluster = d.pop("mainCluster", UNSET)

        family = d.pop("family", UNSET)

        compute = d.pop("compute", UNSET)

        compute_vcpu_hours = d.pop("computeVcpuHours", UNSET)

        compute_credits = d.pop("computeCredits", UNSET)

        out_same_region = d.pop("outSameRegion", UNSET)

        out_same_region_credits = d.pop("outSameRegionCredits", UNSET)

        out_different_region = d.pop("outDifferentRegion", UNSET)

        out_different_region_credits = d.pop("outDifferentRegionCredits", UNSET)

        out_internet = d.pop("outInternet", UNSET)

        out_internet_credits = d.pop("outInternetCredits", UNSET)

        usage_cluster = cls(
            id=id,
            size=size,
            name=name,
            main_cluster=main_cluster,
            family=family,
            compute=compute,
            compute_vcpu_hours=compute_vcpu_hours,
            compute_credits=compute_credits,
            out_same_region=out_same_region,
            out_same_region_credits=out_same_region_credits,
            out_different_region=out_different_region,
            out_different_region_credits=out_different_region_credits,
            out_internet=out_internet,
            out_internet_credits=out_internet_credits,
        )

        return usage_cluster
