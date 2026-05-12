from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="Version")


@_attrs_define
class Version:
    """
    Attributes:
        ui_backend (str):
    """

    ui_backend: str

    def to_dict(self) -> dict[str, Any]:
        ui_backend = self.ui_backend

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ui-backend": ui_backend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ui_backend = d.pop("ui-backend")

        version = cls(
            ui_backend=ui_backend,
        )

        return version
