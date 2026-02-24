from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.auto_stop import AutoStop
    from ..models.cluster_settings_update import ClusterSettingsUpdate


T = TypeVar("T", bound="UpdateCluster")


@_attrs_define
class UpdateCluster:
    """
    Attributes:
        name (str | Unset):
        auto_stop (AutoStop | Unset):
        settings (ClusterSettingsUpdate | Unset):
    """

    name: str | Unset = UNSET
    auto_stop: AutoStop | Unset = UNSET
    settings: ClusterSettingsUpdate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auto_stop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_stop, Unset):
            auto_stop = self.auto_stop.to_dict()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if auto_stop is not UNSET:
            field_dict["autoStop"] = auto_stop
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_stop import AutoStop
        from ..models.cluster_settings_update import ClusterSettingsUpdate

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _auto_stop = d.pop("autoStop", UNSET)
        auto_stop: AutoStop | Unset
        if isinstance(_auto_stop, Unset):
            auto_stop = UNSET
        else:
            auto_stop = AutoStop.from_dict(_auto_stop)

        _settings = d.pop("settings", UNSET)
        settings: ClusterSettingsUpdate | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ClusterSettingsUpdate.from_dict(_settings)

        update_cluster = cls(
            name=name,
            auto_stop=auto_stop,
            settings=settings,
        )

        return update_cluster
