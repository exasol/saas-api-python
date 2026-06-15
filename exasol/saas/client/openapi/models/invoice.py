from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.invoice_dunning_status import InvoiceDunningStatus
from ..models.invoice_price_type import InvoicePriceType
from ..models.invoice_status import InvoiceStatus

T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        amount_paid (int):
        credits_applied (int):
        amount_due (int):
        currency_code (str):
        paid_on (datetime.datetime):
        date (datetime.datetime):
        due_date (datetime.datetime):
        id (str):
        status (InvoiceStatus):
        dunning_status (InvoiceDunningStatus):
        price_type (InvoicePriceType):
    """

    amount_paid: int
    credits_applied: int
    amount_due: int
    currency_code: str
    paid_on: datetime.datetime
    date: datetime.datetime
    due_date: datetime.datetime
    id: str
    status: InvoiceStatus
    dunning_status: InvoiceDunningStatus
    price_type: InvoicePriceType

    def to_dict(self) -> dict[str, Any]:
        amount_paid = self.amount_paid

        credits_applied = self.credits_applied

        amount_due = self.amount_due

        currency_code = self.currency_code

        paid_on = self.paid_on.isoformat()

        date = self.date.isoformat()

        due_date = self.due_date.isoformat()

        id = self.id

        status = self.status.value

        dunning_status = self.dunning_status.value

        price_type = self.price_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amountPaid": amount_paid,
                "creditsApplied": credits_applied,
                "amountDue": amount_due,
                "currencyCode": currency_code,
                "paidOn": paid_on,
                "date": date,
                "dueDate": due_date,
                "id": id,
                "status": status,
                "dunningStatus": dunning_status,
                "priceType": price_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_paid = d.pop("amountPaid")

        credits_applied = d.pop("creditsApplied")

        amount_due = d.pop("amountDue")

        currency_code = d.pop("currencyCode")

        paid_on = isoparse(d.pop("paidOn"))

        date = isoparse(d.pop("date"))

        due_date = isoparse(d.pop("dueDate"))

        id = d.pop("id")

        status = InvoiceStatus(d.pop("status"))

        dunning_status = InvoiceDunningStatus(d.pop("dunningStatus"))

        price_type = InvoicePriceType(d.pop("priceType"))

        invoice = cls(
            amount_paid=amount_paid,
            credits_applied=credits_applied,
            amount_due=amount_due,
            currency_code=currency_code,
            paid_on=paid_on,
            date=date,
            due_date=due_date,
            id=id,
            status=status,
            dunning_status=dunning_status,
            price_type=price_type,
        )

        return invoice
