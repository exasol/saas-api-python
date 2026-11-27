from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.patch_user_databases_add_item_type_1 import (
        PatchUserDatabasesAddItemType1,
    )
    from ..models.patch_user_databases_update_item import PatchUserDatabasesUpdateItem


T = TypeVar("T", bound="PatchUserDatabases")


@_attrs_define
class PatchUserDatabases:
    """
    Attributes:
        delete (list[str] | Unset):
        add (list[PatchUserDatabasesAddItemType1 | str] | Unset):
        update (list[PatchUserDatabasesUpdateItem] | Unset): Changes the user's permission on databases already assigned
            to them.
    """

    delete: list[str] | Unset = UNSET
    add: list[PatchUserDatabasesAddItemType1 | str] | Unset = UNSET
    update: list[PatchUserDatabasesUpdateItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_user_databases_add_item_type_1 import (
            PatchUserDatabasesAddItemType1,
        )

        delete: list[str] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete

        add: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.add, Unset):
            add = []
            for add_item_data in self.add:
                add_item: dict[str, Any] | str
                if isinstance(add_item_data, PatchUserDatabasesAddItemType1):
                    add_item = add_item_data.to_dict()
                else:
                    add_item = add_item_data
                add.append(add_item)

        update: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = []
            for update_item_data in self.update:
                update_item = update_item_data.to_dict()
                update.append(update_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delete is not UNSET:
            field_dict["delete"] = delete
        if add is not UNSET:
            field_dict["add"] = add
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_user_databases_add_item_type_1 import (
            PatchUserDatabasesAddItemType1,
        )
        from ..models.patch_user_databases_update_item import (
            PatchUserDatabasesUpdateItem,
        )

        d = dict(src_dict)
        delete = cast(list[str], d.pop("delete", UNSET))

        _add = d.pop("add", UNSET)
        add: list[PatchUserDatabasesAddItemType1 | str] | Unset = UNSET
        if _add is not UNSET:
            add = []
            for add_item_data in _add:

                def _parse_add_item(
                    data: object,
                ) -> PatchUserDatabasesAddItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        add_item_type_1 = PatchUserDatabasesAddItemType1.from_dict(data)

                        return add_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(PatchUserDatabasesAddItemType1 | str, data)

                add_item = _parse_add_item(add_item_data)

                add.append(add_item)

        _update = d.pop("update", UNSET)
        update: list[PatchUserDatabasesUpdateItem] | Unset = UNSET
        if _update is not UNSET:
            update = []
            for update_item_data in _update:
                update_item = PatchUserDatabasesUpdateItem.from_dict(update_item_data)

                update.append(update_item)

        patch_user_databases = cls(
            delete=delete,
            add=add,
            update=update,
        )

        return patch_user_databases
