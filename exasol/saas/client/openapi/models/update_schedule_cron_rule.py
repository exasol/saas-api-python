from collections.abc import (
    Generator,
    Mapping,
)
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Optional,
    TextIO,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="UpdateScheduleCronRule")


@_attrs_define
class UpdateScheduleCronRule:
    """
    Attributes:
        cron_rule (str): cron rule in format: <minute> <hour> <day> <month> <weekday>
    """

    cron_rule: str

    def to_dict(self) -> dict[str, Any]:
        cron_rule = self.cron_rule

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cronRule": cron_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cron_rule = d.pop("cronRule")

        update_schedule_cron_rule = cls(
            cron_rule=cron_rule,
        )

        return update_schedule_cron_rule
