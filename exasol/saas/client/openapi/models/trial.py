from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Trial")


@_attrs_define
class Trial:
    """
    Attributes:
        expires_at (str):
        remaining_credits (float):
    """

    expires_at: str
    remaining_credits: float

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        remaining_credits = self.remaining_credits

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expiresAt": expires_at,
                "remainingCredits": remaining_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expiresAt")

        remaining_credits = d.pop("remainingCredits")

        trial = cls(
            expires_at=expires_at,
            remaining_credits=remaining_credits,
        )

        return trial
