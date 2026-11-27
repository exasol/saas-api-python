from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.patch_user_databases_add_item_type_1_permission import (
    PatchUserDatabasesAddItemType1Permission,
)
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="PatchUserDatabasesAddItemType1")


@_attrs_define
class PatchUserDatabasesAddItemType1:
    """
    Attributes:
        id (str):
        permission (PatchUserDatabasesAddItemType1Permission | Unset): Access level on this database. Defaults to admin
            when omitted.
    """

    id: str
    permission: PatchUserDatabasesAddItemType1Permission | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _permission = d.pop("permission", UNSET)
        permission: PatchUserDatabasesAddItemType1Permission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = PatchUserDatabasesAddItemType1Permission(_permission)

        patch_user_databases_add_item_type_1 = cls(
            id=id,
            permission=permission,
        )

        return patch_user_databases_add_item_type_1
