from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClusterConnectionIps")


@_attrs_define
class ClusterConnectionIps:
    """
    Attributes:
        private (list[str]):
        public (list[str]):
    """

    private: list[str]
    public: list[str]

    def to_dict(self) -> dict[str, Any]:
        private = self.private

        public = self.public

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "private": private,
                "public": public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private = cast(list[str], d.pop("private"))

        public = cast(list[str], d.pop("public"))

        cluster_connection_ips = cls(
            private=private,
            public=public,
        )

        return cluster_connection_ips
