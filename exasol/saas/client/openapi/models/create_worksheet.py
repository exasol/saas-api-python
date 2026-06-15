from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateWorksheet")


@_attrs_define
class CreateWorksheet:
    """
    Attributes:
        name (str):
        content (str):
        database_id (str):
        cluster_id (str):
    """

    name: str
    content: str
    database_id: str
    cluster_id: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        content = self.content

        database_id = self.database_id

        cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "content": content,
                "databaseId": database_id,
                "clusterId": cluster_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        content = d.pop("content")

        database_id = d.pop("databaseId")

        cluster_id = d.pop("clusterId")

        create_worksheet = cls(
            name=name,
            content=content,
            database_id=database_id,
            cluster_id=cluster_id,
        )

        return create_worksheet
