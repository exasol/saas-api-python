from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="SetAutoUpdatesDatabase")


@_attrs_define
class SetAutoUpdatesDatabase:
    """ 
        Attributes:
            auto_updates_enabled (bool):
     """

    auto_updates_enabled: bool


    def to_dict(self) -> Dict[str, Any]:
        auto_updates_enabled = self.auto_updates_enabled


        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "autoUpdatesEnabled": auto_updates_enabled,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_updates_enabled = d.pop("autoUpdatesEnabled")

        set_auto_updates_database = cls(
            auto_updates_enabled=auto_updates_enabled,
        )

        return set_auto_updates_database

