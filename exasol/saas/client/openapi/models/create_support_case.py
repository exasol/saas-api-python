from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..models.case_priority import CasePriority
from ..models.case_type import CaseType
from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="CreateSupportCase")


@_attrs_define
class CreateSupportCase:
    """
    Attributes:
        case_type (CaseType):
        subject (str):
        description (str):
        emails (str):
        priority (CasePriority | Unset): Priority of the case. critical = 1, major = 2, normal = 3, minor = 4
    """

    case_type: CaseType
    subject: str
    description: str
    emails: str
    priority: CasePriority | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        case_type = self.case_type.value

        subject = self.subject

        description = self.description

        emails = self.emails

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "caseType": case_type,
                "subject": subject,
                "description": description,
                "emails": emails,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        case_type = CaseType(d.pop("caseType"))

        subject = d.pop("subject")

        description = d.pop("description")

        emails = d.pop("emails")

        _priority = d.pop("priority", UNSET)
        priority: CasePriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CasePriority(_priority)

        create_support_case = cls(
            case_type=case_type,
            subject=subject,
            description=description,
            emails=emails,
            priority=priority,
        )

        return create_support_case
