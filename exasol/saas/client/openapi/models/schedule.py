from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.schedule_action_type_0 import ScheduleActionType0
from ..models.schedule_state import ScheduleState
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cluster_action_scale import ClusterActionScale
  from ..models.cluster_action_start_stop import ClusterActionStartStop





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
            payload (ClusterActionScale | ClusterActionStartStop | Unset):
            state (ScheduleState | Unset):
     """

    action: ScheduleActionType0
    cron_rule: str
    id: str | Unset = UNSET
    createdby_id: str | Unset = UNSET
    createdby_first_name: str | Unset = UNSET
    createdby_last_name: str | Unset = UNSET
    cluster_name: str | Unset = UNSET
    payload: ClusterActionScale | ClusterActionStartStop | Unset = UNSET
    state: ScheduleState | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.cluster_action_start_stop import ClusterActionStartStop
        from ..models.cluster_action_scale import ClusterActionScale
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
        elif isinstance(self.payload, ClusterActionScale):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()


        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
            "cronRule": cron_rule,
        })
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
        from ..models.cluster_action_scale import ClusterActionScale
        from ..models.cluster_action_start_stop import ClusterActionStartStop
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

        def _parse_payload(data: object) -> ClusterActionScale | ClusterActionStartStop | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = ClusterActionScale.from_dict(data)



                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            payload_type_1 = ClusterActionStartStop.from_dict(data)



            return payload_type_1

        payload = _parse_payload(d.pop("payload", UNSET))


        _state = d.pop("state", UNSET)
        state: ScheduleState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = ScheduleState(_state)




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

