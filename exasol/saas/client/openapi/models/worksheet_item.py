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
    from ..models.worksheet_item_cluster import WorksheetItemCluster
    from ..models.worksheet_item_database import WorksheetItemDatabase


T = TypeVar("T", bound="WorksheetItem")


@_attrs_define
class WorksheetItem:
    """
    Attributes:
        id (str):
        name (str):
        database (WorksheetItemDatabase):
        cluster (WorksheetItemCluster):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    name: str
    database: WorksheetItemDatabase
    cluster: WorksheetItemCluster
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        database = self.database.to_dict()

        cluster = self.cluster.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
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
        from ..models.worksheet_item_cluster import WorksheetItemCluster
        from ..models.worksheet_item_database import WorksheetItemDatabase

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        database = WorksheetItemDatabase.from_dict(d.pop("database"))

        cluster = WorksheetItemCluster.from_dict(d.pop("cluster"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        worksheet_item = cls(
            id=id,
            name=name,
            database=database,
            cluster=cluster,
            created_at=created_at,
            updated_at=updated_at,
        )

        return worksheet_item
