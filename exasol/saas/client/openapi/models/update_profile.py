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

T = TypeVar("T", bound="UpdateProfile")


@_attrs_define
class UpdateProfile:
    """ 
        Attributes:
            first_name (str):
            last_name (str):
     """

    first_name: str
    last_name: str


    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name


        field_dict: Dict[str, Any] = {}
        field_dict.update({
            "firstName": first_name,
            "lastName": last_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        update_profile = cls(
            first_name=first_name,
            last_name=last_name,
        )

        return update_profile

