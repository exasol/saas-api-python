from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Stream")


@_attrs_define
class Stream:
    """
    Attributes:
        stream_type (str):
        name (str):
        description (str):
    """

    stream_type: str
    name: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        stream_type = self.stream_type

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "stream_type": stream_type,
                "name": name,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stream_type = d.pop("stream_type")

        name = d.pop("name")

        description = d.pop("description")

        stream = cls(
            stream_type=stream_type,
            name=name,
            description=description,
        )

        return stream
