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


T = TypeVar("T", bound="AcceptInvitation")


@_attrs_define
class AcceptInvitation:
    """
    Attributes:
        email (str):
        role_id (str):
        db_username (str):
        user_id (str):
        databases (list[WorksheetConnection] | Unset):
        migrated_user_id (str | Unset):
    """

    email: str
    role_id: str
    db_username: str
    user_id: str
    databases: list[WorksheetConnection] | Unset = UNSET
    migrated_user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role_id = self.role_id

        db_username = self.db_username

        user_id = self.user_id

        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()
                databases.append(databases_item)

        migrated_user_id = self.migrated_user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "roleID": role_id,
                "dbUsername": db_username,
                "userID": user_id,
            }
        )
        if databases is not UNSET:
            field_dict["databases"] = databases
        if migrated_user_id is not UNSET:
            field_dict["migratedUserId"] = migrated_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worksheet_connection import WorksheetConnection

        d = dict(src_dict)
        email = d.pop("email")

        role_id = d.pop("roleID")

        db_username = d.pop("dbUsername")

        user_id = d.pop("userID")

        _databases = d.pop("databases", UNSET)
        databases: list[WorksheetConnection] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for databases_item_data in _databases:
                databases_item = WorksheetConnection.from_dict(databases_item_data)

                databases.append(databases_item)

        migrated_user_id = d.pop("migratedUserId", UNSET)

        accept_invitation = cls(
            email=email,
            role_id=role_id,
            db_username=db_username,
            user_id=user_id,
            databases=databases,
            migrated_user_id=migrated_user_id,
        )

        return accept_invitation
