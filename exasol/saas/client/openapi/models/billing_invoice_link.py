from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="BillingInvoiceLink")


@_attrs_define
class BillingInvoiceLink:
    """
    Attributes:
        link (str):
    """

    link: str

    def to_dict(self) -> dict[str, Any]:
        link = self.link

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "link": link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link = d.pop("link")

        billing_invoice_link = cls(
            link=link,
        )

        return billing_invoice_link
