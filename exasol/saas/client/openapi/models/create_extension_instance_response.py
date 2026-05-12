from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateExtensionInstanceResponse")


@_attrs_define
class CreateExtensionInstanceResponse:
    """
    Attributes:
        instance_id (str):
        instance_name (str):
    """

    instance_id: str
    instance_name: str

    def to_dict(self) -> dict[str, Any]:
        instance_id = self.instance_id

        instance_name = self.instance_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "instanceId": instance_id,
                "instanceName": instance_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_id = d.pop("instanceId")

        instance_name = d.pop("instanceName")

        create_extension_instance_response = cls(
            instance_id=instance_id,
            instance_name=instance_name,
        )

        return create_extension_instance_response
