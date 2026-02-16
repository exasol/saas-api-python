from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateAllowedIP")


@_attrs_define
class UpdateAllowedIP:
    """
    Attributes:
        name (str):
        cidr_ip (str):
    """

    name: str
    cidr_ip: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cidr_ip = self.cidr_ip

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "cidrIp": cidr_ip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        cidr_ip = d.pop("cidrIp")

        update_allowed_ip = cls(
            name=name,
            cidr_ip=cidr_ip,
        )

        return update_allowed_ip
