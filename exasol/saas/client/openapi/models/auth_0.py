from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Auth0")


@_attrs_define
class Auth0:
    """
    Attributes:
        domain (str):
        client_id (str):
        audience (str):
    """

    domain: str
    client_id: str
    audience: str

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        client_id = self.client_id

        audience = self.audience

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
                "clientId": client_id,
                "audience": audience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        client_id = d.pop("clientId")

        audience = d.pop("audience")

        auth_0 = cls(
            domain=domain,
            client_id=client_id,
            audience=audience,
        )

        return auth_0
