from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Credits")


@_attrs_define
class Credits:
    """
    Attributes:
        credit (float):
        usage (float):
        total_usage (float):
    """

    credit: float
    usage: float
    total_usage: float

    def to_dict(self) -> dict[str, Any]:
        credit = self.credit

        usage = self.usage

        total_usage = self.total_usage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credit": credit,
                "usage": usage,
                "totalUsage": total_usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit = d.pop("credit")

        usage = d.pop("usage")

        total_usage = d.pop("totalUsage")

        credits_ = cls(
            credit=credit,
            usage=usage,
            total_usage=total_usage,
        )

        return credits_
