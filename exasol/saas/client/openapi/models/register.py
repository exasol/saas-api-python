from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.register_signup_path import RegisterSignupPath
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="Register")


@_attrs_define
class Register:
    """
    Attributes:
        identifier (str):
        company (str):
        country (str):
        email (str):
        invitation (str | Unset):
        signup_path (RegisterSignupPath | Unset):
    """

    identifier: str
    company: str
    country: str
    email: str
    invitation: str | Unset = UNSET
    signup_path: RegisterSignupPath | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        company = self.company

        country = self.country

        email = self.email

        invitation = self.invitation

        signup_path: str | Unset = UNSET
        if not isinstance(self.signup_path, Unset):
            signup_path = self.signup_path.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identifier": identifier,
                "company": company,
                "country": country,
                "email": email,
            }
        )
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if signup_path is not UNSET:
            field_dict["signupPath"] = signup_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        company = d.pop("company")

        country = d.pop("country")

        email = d.pop("email")

        invitation = d.pop("invitation", UNSET)

        _signup_path = d.pop("signupPath", UNSET)
        signup_path: RegisterSignupPath | Unset
        if isinstance(_signup_path, Unset):
            signup_path = UNSET
        else:
            signup_path = RegisterSignupPath(_signup_path)

        register = cls(
            identifier=identifier,
            company=company,
            country=country,
            email=email,
            invitation=invitation,
            signup_path=signup_path,
        )

        return register
