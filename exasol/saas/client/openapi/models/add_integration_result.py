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

T = TypeVar("T", bound="AddIntegrationResult")


@_attrs_define
class AddIntegrationResult:
    """
    Attributes:
        encrypted_password (str):
        action_url (str):
        encrypted_pat (str | Unset):
    """

    encrypted_password: str
    action_url: str
    encrypted_pat: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        encrypted_password = self.encrypted_password

        action_url = self.action_url

        encrypted_pat = self.encrypted_pat

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "encryptedPassword": encrypted_password,
                "actionUrl": action_url,
            }
        )
        if encrypted_pat is not UNSET:
            field_dict["encryptedPat"] = encrypted_pat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encrypted_password = d.pop("encryptedPassword")

        action_url = d.pop("actionUrl")

        encrypted_pat = d.pop("encryptedPat", UNSET)

        add_integration_result = cls(
            encrypted_password=encrypted_password,
            action_url=action_url,
            encrypted_pat=encrypted_pat,
        )

        return add_integration_result
