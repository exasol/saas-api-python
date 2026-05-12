from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="EmailValidation")


@_attrs_define
class EmailValidation:
    """
    Attributes:
        is_valid (bool):
        is_university (bool):
    """

    is_valid: bool
    is_university: bool

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        is_university = self.is_university

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isValid": is_valid,
                "isUniversity": is_university,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("isValid")

        is_university = d.pop("isUniversity")

        email_validation = cls(
            is_valid=is_valid,
            is_university=is_university,
        )

        return email_validation
