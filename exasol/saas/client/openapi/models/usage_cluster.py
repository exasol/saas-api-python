from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsageCluster")



@_attrs_define
class UsageCluster:
    """ 
        Attributes:
            id (str):
            size (str):
            name (str):
            compute (float | Unset):
            out_same_region (float | Unset):
            out_different_region (float | Unset):
            out_internet (float | Unset):
     """

    id: str
    size: str
    name: str
    compute: float | Unset = UNSET
    out_same_region: float | Unset = UNSET
    out_different_region: float | Unset = UNSET
    out_internet: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        size = self.size

        name = self.name

        compute = self.compute

        out_same_region = self.out_same_region

        out_different_region = self.out_different_region

        out_internet = self.out_internet


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "size": size,
            "name": name,
        })
        if compute is not UNSET:
            field_dict["compute"] = compute
        if out_same_region is not UNSET:
            field_dict["outSameRegion"] = out_same_region
        if out_different_region is not UNSET:
            field_dict["outDifferentRegion"] = out_different_region
        if out_internet is not UNSET:
            field_dict["outInternet"] = out_internet

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        size = d.pop("size")

        name = d.pop("name")

        compute = d.pop("compute", UNSET)

        out_same_region = d.pop("outSameRegion", UNSET)

        out_different_region = d.pop("outDifferentRegion", UNSET)

        out_internet = d.pop("outInternet", UNSET)

        usage_cluster = cls(
            id=id,
            size=size,
            name=name,
            compute=compute,
            out_same_region=out_same_region,
            out_different_region=out_different_region,
            out_internet=out_internet,
        )

        return usage_cluster

