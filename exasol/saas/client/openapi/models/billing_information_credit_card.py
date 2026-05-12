from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.credit_card_status import CreditCardStatus

T = TypeVar("T", bound="BillingInformationCreditCard")


@_attrs_define
class BillingInformationCreditCard:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (CreditCardStatus):
        masked_number (str):
        last4 (str):
        brand (str):
        expiry_year (int):
        expiry_month (int):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: CreditCardStatus
    masked_number: str
    last4: str
    brand: str
    expiry_year: int
    expiry_month: int

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status = self.status.value

        masked_number = self.masked_number

        last4 = self.last4

        brand = self.brand

        expiry_year = self.expiry_year

        expiry_month = self.expiry_month

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
                "status": status,
                "maskedNumber": masked_number,
                "last4": last4,
                "brand": brand,
                "expiryYear": expiry_year,
                "expiryMonth": expiry_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        status = CreditCardStatus(d.pop("status"))

        masked_number = d.pop("maskedNumber")

        last4 = d.pop("last4")

        brand = d.pop("brand")

        expiry_year = d.pop("expiryYear")

        expiry_month = d.pop("expiryMonth")

        billing_information_credit_card = cls(
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            masked_number=masked_number,
            last4=last4,
            brand=brand,
            expiry_year=expiry_year,
            expiry_month=expiry_month,
        )

        return billing_information_credit_card
