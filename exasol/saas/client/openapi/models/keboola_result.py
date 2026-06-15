from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeboolaResult")


@_attrs_define
class KeboolaResult:
    """
    Attributes:
        exa_host (str):
        exa_port (str):
        exa_user_name (str):
        db_name (str):
        exa_password (str):
        email (str):
    """

    exa_host: str
    exa_port: str
    exa_user_name: str
    db_name: str
    exa_password: str
    email: str

    def to_dict(self) -> dict[str, Any]:
        exa_host = self.exa_host

        exa_port = self.exa_port

        exa_user_name = self.exa_user_name

        db_name = self.db_name

        exa_password = self.exa_password

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "exaHost": exa_host,
                "exaPort": exa_port,
                "exaUserName": exa_user_name,
                "dbName": db_name,
                "exaPassword": exa_password,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exa_host = d.pop("exaHost")

        exa_port = d.pop("exaPort")

        exa_user_name = d.pop("exaUserName")

        db_name = d.pop("dbName")

        exa_password = d.pop("exaPassword")

        email = d.pop("email")

        keboola_result = cls(
            exa_host=exa_host,
            exa_port=exa_port,
            exa_user_name=exa_user_name,
            db_name=db_name,
            exa_password=exa_password,
            email=email,
        )

        return keboola_result
