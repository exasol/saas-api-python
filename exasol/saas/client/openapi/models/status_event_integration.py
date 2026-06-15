from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusEventIntegration")


@_attrs_define
class StatusEventIntegration:
    """
    Attributes:
        organization_id (str):
        database_id (str):
        cluster_id (str):
        status (str):
        url (str):
    """

    organization_id: str
    database_id: str
    cluster_id: str
    status: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        database_id = self.database_id

        cluster_id = self.cluster_id

        status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationId": organization_id,
                "databaseId": database_id,
                "clusterId": cluster_id,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organizationId")

        database_id = d.pop("databaseId")

        cluster_id = d.pop("clusterId")

        status = d.pop("status")

        url = d.pop("url")

        status_event_integration = cls(
            organization_id=organization_id,
            database_id=database_id,
            cluster_id=cluster_id,
            status=status,
            url=url,
        )

        status_event_integration.additional_properties = d
        return status_event_integration

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
