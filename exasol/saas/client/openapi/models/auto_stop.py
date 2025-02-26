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

T = TypeVar("T", bound="AutoStop")


@_attrs_define
class AutoStop:
    """ 
        Attributes:
            enabled (bool):
            idle_time (int):
     """

    enabled: bool
    idle_time: int


    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        idle_time = self.idle_time


        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "enabled": enabled,
            "idleTime": idle_time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled")

        idle_time = d.pop("idleTime")

        auto_stop = cls(
            enabled=enabled,
            idle_time=idle_time,
        )

        return auto_stop

