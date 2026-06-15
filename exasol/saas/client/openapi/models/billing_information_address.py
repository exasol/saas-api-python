from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.billing_address_status import BillingAddressStatus
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="BillingInformationAddress")


@_attrs_define
class BillingInformationAddress:
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
        validation_status (BillingAddressStatus):
        state (str | Unset):
        vat_number (str | Unset):
    """

    first_name: str
    last_name: str
    email: str
    company: str
    line1: str
    city: str
    country: str
    zip_: str
    validation_status: BillingAddressStatus
    state: str | Unset = UNSET
    vat_number: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        company = self.company

        line1 = self.line1

        city = self.city

        country = self.country

        zip_ = self.zip_

        validation_status = self.validation_status.value

        state = self.state

        vat_number = self.vat_number

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
                "validationStatus": validation_status,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number

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

        validation_status = BillingAddressStatus(d.pop("validationStatus"))

        state = d.pop("state", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        billing_information_address = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            line1=line1,
            city=city,
            country=country,
            zip_=zip_,
            validation_status=validation_status,
            state=state,
            vat_number=vat_number,
        )

        return billing_information_address
