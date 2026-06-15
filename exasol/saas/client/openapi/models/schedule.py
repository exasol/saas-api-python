from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.schedule_action_type_0 import ScheduleActionType0
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.schedule_payload_type_0 import SchedulePayloadType0
    from ..models.schedule_payload_type_1 import SchedulePayloadType1


T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """
    Attributes:
        action (ScheduleActionType0):
        cron_rule (str): cron rule in format: <minute> <hour> <day> <month> <weekday>
        id (str | Unset):
        createdby_id (str | Unset):
        createdby_first_name (str | Unset):
        createdby_last_name (str | Unset):
        cluster_name (str | Unset):
        payload (SchedulePayloadType0 | SchedulePayloadType1 | Unset):
        state (str | Unset):  Default: 'ENABLED'.
    """

    action: ScheduleActionType0
    cron_rule: str
    id: str | Unset = UNSET
    createdby_id: str | Unset = UNSET
    createdby_first_name: str | Unset = UNSET
    createdby_last_name: str | Unset = UNSET
    cluster_name: str | Unset = UNSET
    payload: SchedulePayloadType0 | SchedulePayloadType1 | Unset = UNSET
    state: str | Unset = "ENABLED"

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_payload_type_0 import SchedulePayloadType0

        action: str
        if isinstance(self.action, ScheduleActionType0):
            action = self.action.value

        cron_rule = self.cron_rule

        id = self.id

        createdby_id = self.createdby_id

        createdby_first_name = self.createdby_first_name

        createdby_last_name = self.createdby_last_name

        cluster_name = self.cluster_name

        payload: dict[str, Any] | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, SchedulePayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "cronRule": cron_rule,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if createdby_id is not UNSET:
            field_dict["createdbyID"] = createdby_id
        if createdby_first_name is not UNSET:
            field_dict["createdbyFirstName"] = createdby_first_name
        if createdby_last_name is not UNSET:
            field_dict["createdbyLastName"] = createdby_last_name
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if payload is not UNSET:
            field_dict["payload"] = payload
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_payload_type_0 import SchedulePayloadType0
        from ..models.schedule_payload_type_1 import SchedulePayloadType1

        d = dict(src_dict)

        def _parse_action(data: object) -> ScheduleActionType0:
            if not isinstance(data, str):
                raise TypeError()
            action_type_0 = ScheduleActionType0(data)

            return action_type_0

        action = _parse_action(d.pop("action"))

        cron_rule = d.pop("cronRule")

        id = d.pop("id", UNSET)

        createdby_id = d.pop("createdbyID", UNSET)

        createdby_first_name = d.pop("createdbyFirstName", UNSET)

        createdby_last_name = d.pop("createdbyLastName", UNSET)

        cluster_name = d.pop("clusterName", UNSET)

        def _parse_payload(
            data: object,
        ) -> SchedulePayloadType0 | SchedulePayloadType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = SchedulePayloadType0.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payload_type_1 = SchedulePayloadType1.from_dict(data)

            return payload_type_1

        payload = _parse_payload(d.pop("payload", UNSET))

        state = d.pop("state", UNSET)

        schedule = cls(
            action=action,
            cron_rule=cron_rule,
            id=id,
            createdby_id=createdby_id,
            createdby_first_name=createdby_first_name,
            createdby_last_name=createdby_last_name,
            cluster_name=cluster_name,
            payload=payload,
            state=state,
        )

        return schedule
