from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="PaymentAttempt")


@_attrs_define
class PaymentAttempt:
    """
    Attributes:
        status (str):
        type_ (str):
        active (bool):
        id_at_gateway (str):
        action_payload (Any):
        error_code (str):
        error_text (str):
        error_msg (str):
    """

    status: str
    type_: str
    active: bool
    id_at_gateway: str
    action_payload: Any
    error_code: str
    error_text: str
    error_msg: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        type_ = self.type_

        active = self.active

        id_at_gateway = self.id_at_gateway

        action_payload = self.action_payload

        error_code = self.error_code

        error_text = self.error_text

        error_msg = self.error_msg

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "type": type_,
                "active": active,
                "id_at_gateway": id_at_gateway,
                "action_payload": action_payload,
                "error_code": error_code,
                "error_text": error_text,
                "error_msg": error_msg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        type_ = d.pop("type")

        active = d.pop("active")

        id_at_gateway = d.pop("id_at_gateway")

        action_payload = d.pop("action_payload")

        error_code = d.pop("error_code")

        error_text = d.pop("error_text")

        error_msg = d.pop("error_msg")

        payment_attempt = cls(
            status=status,
            type_=type_,
            active=active,
            id_at_gateway=id_at_gateway,
            action_payload=action_payload,
            error_code=error_code,
            error_text=error_text,
            error_msg=error_msg,
        )

        return payment_attempt
