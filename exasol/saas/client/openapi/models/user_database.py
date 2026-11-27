from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.user_database_permission import UserDatabasePermission

T = TypeVar("T", bound="UserDatabase")


@_attrs_define
class UserDatabase:
    """
    Attributes:
        id (str):
        name (str):
        permission (UserDatabasePermission): The user's access level on this database.
    """

    id: str
    name: str
    permission: UserDatabasePermission

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        permission = UserDatabasePermission(d.pop("permission"))

        user_database = cls(
            id=id,
            name=name,
            permission=permission,
        )

        return user_database
