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

T = TypeVar("T", bound="SendCsat")


@_attrs_define
class SendCsat:
    """
    Attributes:
        email (str):
        saas_csat_score (float):
        saas_csat_comments (str | Unset):
    """

    email: str
    saas_csat_score: float
    saas_csat_comments: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        saas_csat_score = self.saas_csat_score

        saas_csat_comments = self.saas_csat_comments

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "saas_csat_score": saas_csat_score,
            }
        )
        if saas_csat_comments is not UNSET:
            field_dict["saas_csat_comments"] = saas_csat_comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        saas_csat_score = d.pop("saas_csat_score")

        saas_csat_comments = d.pop("saas_csat_comments", UNSET)

        send_csat = cls(
            email=email,
            saas_csat_score=saas_csat_score,
            saas_csat_comments=saas_csat_comments,
        )

        return send_csat
