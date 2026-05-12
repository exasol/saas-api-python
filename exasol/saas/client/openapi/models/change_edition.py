from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.account_edition import AccountEdition

T = TypeVar("T", bound="ChangeEdition")


@_attrs_define
class ChangeEdition:
    """
    Attributes:
        edition (AccountEdition):
    """

    edition: AccountEdition

    def to_dict(self) -> dict[str, Any]:
        edition = self.edition.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "edition": edition,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edition = AccountEdition(d.pop("edition"))

        change_edition = cls(
            edition=edition,
        )

        return change_edition
