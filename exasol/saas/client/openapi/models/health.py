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
    from ..models.health_checks import HealthChecks
    from ..models.health_links import HealthLinks


T = TypeVar("T", bound="Health")


@_attrs_define
class Health:
    """
    Attributes:
        status (str):
        version (str | Unset):
        release_id (str | Unset):
        notes (list[str] | Unset):
        output (str | Unset):
        checks (HealthChecks | Unset):
        links (HealthLinks | Unset):
        service_id (str | Unset):
        description (str | Unset):
    """

    status: str
    version: str | Unset = UNSET
    release_id: str | Unset = UNSET
    notes: list[str] | Unset = UNSET
    output: str | Unset = UNSET
    checks: HealthChecks | Unset = UNSET
    links: HealthLinks | Unset = UNSET
    service_id: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        version = self.version

        release_id = self.release_id

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        output = self.output

        checks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        service_id = self.service_id

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if output is not UNSET:
            field_dict["output"] = output
        if checks is not UNSET:
            field_dict["checks"] = checks
        if links is not UNSET:
            field_dict["links"] = links
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_checks import HealthChecks
        from ..models.health_links import HealthLinks

        d = dict(src_dict)
        status = d.pop("status")

        version = d.pop("version", UNSET)

        release_id = d.pop("releaseId", UNSET)

        notes = cast(list[str], d.pop("notes", UNSET))

        output = d.pop("output", UNSET)

        _checks = d.pop("checks", UNSET)
        checks: HealthChecks | Unset
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = HealthChecks.from_dict(_checks)

        _links = d.pop("links", UNSET)
        links: HealthLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = HealthLinks.from_dict(_links)

        service_id = d.pop("serviceId", UNSET)

        description = d.pop("description", UNSET)

        health = cls(
            status=status,
            version=version,
            release_id=release_id,
            notes=notes,
            output=output,
            checks=checks,
            links=links,
            service_id=service_id,
            description=description,
        )

        return health
