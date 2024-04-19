from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Dict,
    List,
    Optional,
    TextIO,
    Tuple,
    Type,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
  from ..models.usage_database import UsageDatabase





T = TypeVar("T", bound="GetUsageResponse200")


@_attrs_define
class GetUsageResponse200:
    """ 
     """

    additional_properties: Dict[str, List['UsageDatabase']] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.usage_database import UsageDatabase
        
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)





        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.usage_database import UsageDatabase
        d = src_dict.copy()
        get_usage_response_200 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in (_additional_property):
                additional_property_item = UsageDatabase.from_dict(additional_property_item_data)



                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        get_usage_response_200.additional_properties = additional_properties
        return get_usage_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List['UsageDatabase']:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List['UsageDatabase']) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
