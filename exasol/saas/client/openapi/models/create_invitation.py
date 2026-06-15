from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.worksheet_connection import WorksheetConnection


T = TypeVar("T", bound="CreateInvitation")


@_attrs_define
class CreateInvitation:
    """
    Attributes:
        email (str):
        role_id (str):
        db_username (str):
        databases (list[WorksheetConnection] | Unset):
    """

    email: str
    role_id: str
    db_username: str
    databases: list[WorksheetConnection] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role_id = self.role_id

        db_username = self.db_username

        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()
                databases.append(databases_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "roleID": role_id,
                "dbUsername": db_username,
            }
        )
        if databases is not UNSET:
            field_dict["databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worksheet_connection import WorksheetConnection

        d = dict(src_dict)
        email = d.pop("email")

        role_id = d.pop("roleID")

        db_username = d.pop("dbUsername")

        _databases = d.pop("databases", UNSET)
        databases: list[WorksheetConnection] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for databases_item_data in _databases:
                databases_item = WorksheetConnection.from_dict(databases_item_data)

                databases.append(databases_item)

        create_invitation = cls(
            email=email,
            role_id=role_id,
            db_username=db_username,
            databases=databases,
        )

        return create_invitation
