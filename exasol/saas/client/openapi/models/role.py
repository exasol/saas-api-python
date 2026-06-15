from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.scope import Scope
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        id (str):
        created_at (datetime.datetime):
        created_by (str):
        name (str):
        description (str):
        scopes (list[Scope]):
        custom (bool):
        deleted_by (str | Unset):
        deleted_at (datetime.datetime | Unset):
    """

    id: str
    created_at: datetime.datetime
    created_by: str
    name: str
    description: str
    scopes: list[Scope]
    custom: bool
    deleted_by: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        description = self.description

        scopes = []
        for scopes_item_data in self.scopes:
            scopes_item = scopes_item_data.value
            scopes.append(scopes_item)

        custom = self.custom

        deleted_by = self.deleted_by

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "createdBy": created_by,
                "name": name,
                "description": description,
                "scopes": scopes,
                "custom": custom,
            }
        )
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        name = d.pop("name")

        description = d.pop("description")

        scopes = []
        _scopes = d.pop("scopes")
        for scopes_item_data in _scopes:
            scopes_item = Scope(scopes_item_data)

            scopes.append(scopes_item)

        custom = d.pop("custom")

        deleted_by = d.pop("deletedBy", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        role = cls(
            id=id,
            created_at=created_at,
            created_by=created_by,
            name=name,
            description=description,
            scopes=scopes,
            custom=custom,
            deleted_by=deleted_by,
            deleted_at=deleted_at,
        )

        return role
