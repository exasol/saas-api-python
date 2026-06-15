from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.worksheet_cluster import WorksheetCluster
    from ..models.worksheet_database import WorksheetDatabase


T = TypeVar("T", bound="Worksheet")


@_attrs_define
class Worksheet:
    """
    Attributes:
        content (str):
        id (str):
        name (str):
        database (WorksheetDatabase):
        cluster (WorksheetCluster):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    content: str
    id: str
    name: str
    database: WorksheetDatabase
    cluster: WorksheetCluster
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        id = self.id

        name = self.name

        database = self.database.to_dict()

        cluster = self.cluster.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "id": id,
                "name": name,
                "database": database,
                "cluster": cluster,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worksheet_cluster import WorksheetCluster
        from ..models.worksheet_database import WorksheetDatabase

        d = dict(src_dict)
        content = d.pop("content")

        id = d.pop("id")

        name = d.pop("name")

        database = WorksheetDatabase.from_dict(d.pop("database"))

        cluster = WorksheetCluster.from_dict(d.pop("cluster"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        worksheet = cls(
            content=content,
            id=id,
            name=name,
            database=database,
            cluster=cluster,
            created_at=created_at,
            updated_at=updated_at,
        )

        return worksheet
