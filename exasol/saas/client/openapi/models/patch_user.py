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
    from ..models.patch_user_databases import PatchUserDatabases


T = TypeVar("T", bound="PatchUser")


@_attrs_define
class PatchUser:
    """
    Attributes:
        role_id (str | Unset):
        databases (PatchUserDatabases | Unset):
        db_username (str | Unset):
    """

    role_id: str | Unset = UNSET
    databases: PatchUserDatabases | Unset = UNSET
    db_username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        databases: dict[str, Any] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = self.databases.to_dict()

        db_username = self.db_username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleID"] = role_id
        if databases is not UNSET:
            field_dict["databases"] = databases
        if db_username is not UNSET:
            field_dict["dbUsername"] = db_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_user_databases import PatchUserDatabases

        d = dict(src_dict)
        role_id = d.pop("roleID", UNSET)

        _databases = d.pop("databases", UNSET)
        databases: PatchUserDatabases | Unset
        if isinstance(_databases, Unset):
            databases = UNSET
        else:
            databases = PatchUserDatabases.from_dict(_databases)

        db_username = d.pop("dbUsername", UNSET)

        patch_user = cls(
            role_id=role_id,
            databases=databases,
            db_username=db_username,
        )

        return patch_user
