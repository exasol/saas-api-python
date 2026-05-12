from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="RegisterResult")


@_attrs_define
class RegisterResult:
    """
    Attributes:
        account_id (str):
        invitation_url (str):
    """

    account_id: str
    invitation_url: str

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        invitation_url = self.invitation_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accountId": account_id,
                "invitationUrl": invitation_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        invitation_url = d.pop("invitationUrl")

        register_result = cls(
            account_id=account_id,
            invitation_url=invitation_url,
        )

        return register_result
