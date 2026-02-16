from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.schedule_state import ScheduleState

T = TypeVar("T", bound="UpdateScheduleState")


@_attrs_define
class UpdateScheduleState:
    """
    Attributes:
        state (ScheduleState):
    """

    state: ScheduleState

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = ScheduleState(d.pop("state"))

        update_schedule_state = cls(
            state=state,
        )

        return update_schedule_state
