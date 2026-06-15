from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.payment_attempt import PaymentAttempt


T = TypeVar("T", bound="PaymentIntent")


@_attrs_define
class PaymentIntent:
    """
    Attributes:
        id (str):
        status (str):
        amount (int):
        currency_code (str):
        gateway_account_id (str):
        gateway (str):
        active_payment_attempttype (PaymentAttempt):
        customer_idtype (str):
        reference_idtype (str):
        expires_at (int):
        created_at (int):
        modified_at (int):
        object_ (str):
        payment_method_type (str):
    """

    id: str
    status: str
    amount: int
    currency_code: str
    gateway_account_id: str
    gateway: str
    active_payment_attempttype: PaymentAttempt
    customer_idtype: str
    reference_idtype: str
    expires_at: int
    created_at: int
    modified_at: int
    object_: str
    payment_method_type: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        amount = self.amount

        currency_code = self.currency_code

        gateway_account_id = self.gateway_account_id

        gateway = self.gateway

        active_payment_attempttype = self.active_payment_attempttype.to_dict()

        customer_idtype = self.customer_idtype

        reference_idtype = self.reference_idtype

        expires_at = self.expires_at

        created_at = self.created_at

        modified_at = self.modified_at

        object_ = self.object_

        payment_method_type = self.payment_method_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "status": status,
                "amount": amount,
                "currency_code": currency_code,
                "gateway_account_id": gateway_account_id,
                "gateway": gateway,
                "active_payment_attempttype": active_payment_attempttype,
                "customer_idtype": customer_idtype,
                "reference_idtype": reference_idtype,
                "expires_at": expires_at,
                "created_at": created_at,
                "modified_at": modified_at,
                "object": object_,
                "payment_method_type": payment_method_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_attempt import PaymentAttempt

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        amount = d.pop("amount")

        currency_code = d.pop("currency_code")

        gateway_account_id = d.pop("gateway_account_id")

        gateway = d.pop("gateway")

        active_payment_attempttype = PaymentAttempt.from_dict(
            d.pop("active_payment_attempttype")
        )

        customer_idtype = d.pop("customer_idtype")

        reference_idtype = d.pop("reference_idtype")

        expires_at = d.pop("expires_at")

        created_at = d.pop("created_at")

        modified_at = d.pop("modified_at")

        object_ = d.pop("object")

        payment_method_type = d.pop("payment_method_type")

        payment_intent = cls(
            id=id,
            status=status,
            amount=amount,
            currency_code=currency_code,
            gateway_account_id=gateway_account_id,
            gateway=gateway,
            active_payment_attempttype=active_payment_attempttype,
            customer_idtype=customer_idtype,
            reference_idtype=reference_idtype,
            expires_at=expires_at,
            created_at=created_at,
            modified_at=modified_at,
            object_=object_,
            payment_method_type=payment_method_type,
        )

        return payment_intent
