from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_schedule_payload import CreateSchedulePayload


T = TypeVar("T", bound="CreateSchedule")


@_attrs_define
class CreateSchedule:
    """
    Attributes:
        action (str):
        cron_rule (str):
        payload (CreateSchedulePayload):
    """

    action: str
    cron_rule: str
    payload: CreateSchedulePayload

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        cron_rule = self.cron_rule

        payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "cronRule": cron_rule,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_schedule_payload import CreateSchedulePayload

        d = dict(src_dict)
        action = d.pop("action")

        cron_rule = d.pop("cronRule")

        payload = CreateSchedulePayload.from_dict(d.pop("payload"))

        create_schedule = cls(
            action=action,
            cron_rule=cron_rule,
            payload=payload,
        )

        return create_schedule
