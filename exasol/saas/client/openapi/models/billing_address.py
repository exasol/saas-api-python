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

T = TypeVar("T", bound="BillingAddress")


@_attrs_define
class BillingAddress:
    """
    Attributes:
        first_name (str):
        last_name (str):
        email (str):
        company (str):
        line1 (str):
        city (str):
        country (str):
        zip_ (str):
        vat_number (str):
        state (str | Unset):
    """

    first_name: str
    last_name: str
    email: str
    company: str
    line1: str
    city: str
    country: str
    zip_: str
    vat_number: str
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        company = self.company

        line1 = self.line1

        city = self.city

        country = self.country

        zip_ = self.zip_

        vat_number = self.vat_number

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "company": company,
                "line1": line1,
                "city": city,
                "country": country,
                "zip": zip_,
                "vatNumber": vat_number,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        company = d.pop("company")

        line1 = d.pop("line1")

        city = d.pop("city")

        country = d.pop("country")

        zip_ = d.pop("zip")

        vat_number = d.pop("vatNumber")

        state = d.pop("state", UNSET)

        billing_address = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            line1=line1,
            city=city,
            country=country,
            zip_=zip_,
            vat_number=vat_number,
            state=state,
        )

        return billing_address
