from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.account_edition import AccountEdition
from ..models.account_mode import AccountMode
from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.limits import Limits
    from ..models.trial import Trial


T = TypeVar("T", bound="Account")


@_attrs_define
class Account:
    """
    Attributes:
        id (str):
        email (str):
        created_at (datetime.datetime):
        created_by (str):
        mode (AccountMode):
        edition (AccountEdition):
        limits (Limits):
        account_name (str | Unset):
        country (str | Unset):
        company (str | Unset):
        deleted_at (datetime.datetime | Unset):
        deleted_by (str | Unset):
        edition_locked_for (int | Unset):
        trial (Trial | Unset):
        enabled_features (list[str] | Unset):
    """

    id: str
    email: str
    created_at: datetime.datetime
    created_by: str
    mode: AccountMode
    edition: AccountEdition
    limits: Limits
    account_name: str | Unset = UNSET
    country: str | Unset = UNSET
    company: str | Unset = UNSET
    deleted_at: datetime.datetime | Unset = UNSET
    deleted_by: str | Unset = UNSET
    edition_locked_for: int | Unset = UNSET
    trial: Trial | Unset = UNSET
    enabled_features: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        mode = self.mode.value

        edition = self.edition.value

        limits = self.limits.to_dict()

        account_name = self.account_name

        country = self.country

        company = self.company

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        deleted_by = self.deleted_by

        edition_locked_for = self.edition_locked_for

        trial: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trial, Unset):
            trial = self.trial.to_dict()

        enabled_features: list[str] | Unset = UNSET
        if not isinstance(self.enabled_features, Unset):
            enabled_features = self.enabled_features

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
                "createdAt": created_at,
                "createdBy": created_by,
                "mode": mode,
                "edition": edition,
                "limits": limits,
            }
        )
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if country is not UNSET:
            field_dict["country"] = country
        if company is not UNSET:
            field_dict["company"] = company
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if edition_locked_for is not UNSET:
            field_dict["editionLockedFor"] = edition_locked_for
        if trial is not UNSET:
            field_dict["trial"] = trial
        if enabled_features is not UNSET:
            field_dict["enabledFeatures"] = enabled_features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limits import Limits
        from ..models.trial import Trial

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        mode = AccountMode(d.pop("mode"))

        edition = AccountEdition(d.pop("edition"))

        limits = Limits.from_dict(d.pop("limits"))

        account_name = d.pop("accountName", UNSET)

        country = d.pop("country", UNSET)

        company = d.pop("company", UNSET)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        deleted_by = d.pop("deletedBy", UNSET)

        edition_locked_for = d.pop("editionLockedFor", UNSET)

        _trial = d.pop("trial", UNSET)
        trial: Trial | Unset
        if isinstance(_trial, Unset):
            trial = UNSET
        else:
            trial = Trial.from_dict(_trial)

        enabled_features = cast(list[str], d.pop("enabledFeatures", UNSET))

        account = cls(
            id=id,
            email=email,
            created_at=created_at,
            created_by=created_by,
            mode=mode,
            edition=edition,
            limits=limits,
            account_name=account_name,
            country=country,
            company=company,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            edition_locked_for=edition_locked_for,
            trial=trial,
            enabled_features=enabled_features,
        )

        return account
