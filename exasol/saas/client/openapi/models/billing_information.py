from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.billing_customer import BillingCustomer
    from ..models.billing_information_address import BillingInformationAddress
    from ..models.billing_information_credit_card import BillingInformationCreditCard


T = TypeVar("T", bound="BillingInformation")


@_attrs_define
class BillingInformation:
    """
    Attributes:
        optional_billing (bool):
        billing_address (BillingInformationAddress | Unset):
        card (BillingInformationCreditCard | Unset):
        customer (BillingCustomer | Unset):
    """

    optional_billing: bool
    billing_address: BillingInformationAddress | Unset = UNSET
    card: BillingInformationCreditCard | Unset = UNSET
    customer: BillingCustomer | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        optional_billing = self.optional_billing

        billing_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        customer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "optionalBilling": optional_billing,
            }
        )
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if card is not UNSET:
            field_dict["card"] = card
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_customer import BillingCustomer
        from ..models.billing_information_address import BillingInformationAddress
        from ..models.billing_information_credit_card import (
            BillingInformationCreditCard,
        )

        d = dict(src_dict)
        optional_billing = d.pop("optionalBilling")

        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: BillingInformationAddress | Unset
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BillingInformationAddress.from_dict(_billing_address)

        _card = d.pop("card", UNSET)
        card: BillingInformationCreditCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = BillingInformationCreditCard.from_dict(_card)

        _customer = d.pop("customer", UNSET)
        customer: BillingCustomer | Unset
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = BillingCustomer.from_dict(_customer)

        billing_information = cls(
            optional_billing=optional_billing,
            billing_address=billing_address,
            card=card,
            customer=customer,
        )

        return billing_information
