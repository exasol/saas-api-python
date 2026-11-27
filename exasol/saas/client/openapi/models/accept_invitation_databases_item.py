from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.accept_invitation_databases_item_permission import (
    AcceptInvitationDatabasesItemPermission,
)
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="AcceptInvitationDatabasesItem")


@_attrs_define
class AcceptInvitationDatabasesItem:
    """
    Attributes:
        id (str):
        name (str):
        permission (AcceptInvitationDatabasesItemPermission | Unset): Access level on this database. Defaults to admin
            when omitted.
    """

    id: str
    name: str
    permission: AcceptInvitationDatabasesItemPermission | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _permission = d.pop("permission", UNSET)
        permission: AcceptInvitationDatabasesItemPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = AcceptInvitationDatabasesItemPermission(_permission)

        accept_invitation_databases_item = cls(
            id=id,
            name=name,
            permission=permission,
        )

        return accept_invitation_databases_item
