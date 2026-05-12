from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Chargebee")


@_attrs_define
class Chargebee:
    """
    Attributes:
        site (str):
        api_key (str):
    """

    site: str
    api_key: str

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        api_key = self.api_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "site": site,
                "apiKey": api_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site = d.pop("site")

        api_key = d.pop("apiKey")

        chargebee = cls(
            site=site,
            api_key=api_key,
        )

        return chargebee
