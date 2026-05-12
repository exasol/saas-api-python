from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="BillingCustomer")


@_attrs_define
class BillingCustomer:
    """
    Attributes:
        company (str):
        country (str):
    """

    company: str
    country: str

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        country = self.country

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company": company,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        country = d.pop("country")

        billing_customer = cls(
            company=company,
            country=country,
        )

        return billing_customer
