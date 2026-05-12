from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.id_name import IdName


T = TypeVar("T", bound="Keboola")


@_attrs_define
class Keboola:
    """
    Attributes:
        cluster (IdName):
        database (IdName):
        email (str):
    """

    cluster: IdName
    database: IdName
    email: str

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster.to_dict()

        database = self.database.to_dict()

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cluster": cluster,
                "database": database,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name import IdName

        d = dict(src_dict)
        cluster = IdName.from_dict(d.pop("cluster"))

        database = IdName.from_dict(d.pop("database"))

        email = d.pop("email")

        keboola = cls(
            cluster=cluster,
            database=database,
            email=email,
        )

        return keboola
