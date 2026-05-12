from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.credit_card_status import CreditCardStatus

T = TypeVar("T", bound="CreditCard")


@_attrs_define
class CreditCard:
    """
    Attributes:
        id (str):
        status (CreditCardStatus):
        masked_number (str):
        last4 (str):
        brand (str):
        expire_year (int):
        expire_month (int):
        is_primary (bool):
    """

    id: str
    status: CreditCardStatus
    masked_number: str
    last4: str
    brand: str
    expire_year: int
    expire_month: int
    is_primary: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        masked_number = self.masked_number

        last4 = self.last4

        brand = self.brand

        expire_year = self.expire_year

        expire_month = self.expire_month

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "status": status,
                "maskedNumber": masked_number,
                "last4": last4,
                "brand": brand,
                "expireYear": expire_year,
                "expireMonth": expire_month,
                "isPrimary": is_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = CreditCardStatus(d.pop("status"))

        masked_number = d.pop("maskedNumber")

        last4 = d.pop("last4")

        brand = d.pop("brand")

        expire_year = d.pop("expireYear")

        expire_month = d.pop("expireMonth")

        is_primary = d.pop("isPrimary")

        credit_card = cls(
            id=id,
            status=status,
            masked_number=masked_number,
            last4=last4,
            brand=brand,
            expire_year=expire_year,
            expire_month=expire_month,
            is_primary=is_primary,
        )

        return credit_card
