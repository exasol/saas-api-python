from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddCreditCard")


@_attrs_define
class AddCreditCard:
    """
    Attributes:
        token (str):
        gateway_account_id (str):
        is3ds (bool):
        is_primary (bool):
    """

    token: str
    gateway_account_id: str
    is3ds: bool
    is_primary: bool

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        gateway_account_id = self.gateway_account_id

        is3ds = self.is3ds

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "gatewayAccountID": gateway_account_id,
                "is3ds": is3ds,
                "isPrimary": is_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        gateway_account_id = d.pop("gatewayAccountID")

        is3ds = d.pop("is3ds")

        is_primary = d.pop("isPrimary")

        add_credit_card = cls(
            token=token,
            gateway_account_id=gateway_account_id,
            is3ds=is3ds,
            is_primary=is_primary,
        )

        return add_credit_card
