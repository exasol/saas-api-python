from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.patch_user_databases_update_item_permission import (
    PatchUserDatabasesUpdateItemPermission,
)

T = TypeVar("T", bound="PatchUserDatabasesUpdateItem")


@_attrs_define
class PatchUserDatabasesUpdateItem:
    """
    Attributes:
        id (str):
        permission (PatchUserDatabasesUpdateItemPermission): New access level on this database.
    """

    id: str
    permission: PatchUserDatabasesUpdateItemPermission

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        permission = PatchUserDatabasesUpdateItemPermission(d.pop("permission"))

        patch_user_databases_update_item = cls(
            id=id,
            permission=permission,
        )

        return patch_user_databases_update_item
