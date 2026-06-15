from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.checks_links import ChecksLinks


T = TypeVar("T", bound="Checks")


@_attrs_define
class Checks:
    """
    Attributes:
        status (str):
        component_id (str | Unset):
        component_type (str | Unset):
        observed_value (Any | Unset):
        observed_unit (str | Unset):
        affected_endpoints (list[str] | Unset):
        time (str | Unset):
        output (str | Unset):
        links (ChecksLinks | Unset):
    """

    status: str
    component_id: str | Unset = UNSET
    component_type: str | Unset = UNSET
    observed_value: Any | Unset = UNSET
    observed_unit: str | Unset = UNSET
    affected_endpoints: list[str] | Unset = UNSET
    time: str | Unset = UNSET
    output: str | Unset = UNSET
    links: ChecksLinks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        component_id = self.component_id

        component_type = self.component_type

        observed_value = self.observed_value

        observed_unit = self.observed_unit

        affected_endpoints: list[str] | Unset = UNSET
        if not isinstance(self.affected_endpoints, Unset):
            affected_endpoints = self.affected_endpoints

        time = self.time

        output = self.output

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if component_type is not UNSET:
            field_dict["componentType"] = component_type
        if observed_value is not UNSET:
            field_dict["observedValue"] = observed_value
        if observed_unit is not UNSET:
            field_dict["observedUnit"] = observed_unit
        if affected_endpoints is not UNSET:
            field_dict["affectedEndpoints"] = affected_endpoints
        if time is not UNSET:
            field_dict["time"] = time
        if output is not UNSET:
            field_dict["output"] = output
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checks_links import ChecksLinks

        d = dict(src_dict)
        status = d.pop("status")

        component_id = d.pop("componentId", UNSET)

        component_type = d.pop("componentType", UNSET)

        observed_value = d.pop("observedValue", UNSET)

        observed_unit = d.pop("observedUnit", UNSET)

        affected_endpoints = cast(list[str], d.pop("affectedEndpoints", UNSET))

        time = d.pop("time", UNSET)

        output = d.pop("output", UNSET)

        _links = d.pop("links", UNSET)
        links: ChecksLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ChecksLinks.from_dict(_links)

        checks = cls(
            status=status,
            component_id=component_id,
            component_type=component_type,
            observed_value=observed_value,
            observed_unit=observed_unit,
            affected_endpoints=affected_endpoints,
            time=time,
            output=output,
            links=links,
        )

        return checks
