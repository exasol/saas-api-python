from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="PatchUserDatabases")


@_attrs_define
class PatchUserDatabases:
    """
    Attributes:
        delete (list[str]):
        add (list[str]):
    """

    delete: list[str]
    add: list[str]

    def to_dict(self) -> dict[str, Any]:
        delete = self.delete

        add = self.add

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delete": delete,
                "add": add,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete = cast(list[str], d.pop("delete"))

        add = cast(list[str], d.pop("add"))

        patch_user_databases = cls(
            delete=delete,
            add=add,
        )

        return patch_user_databases
