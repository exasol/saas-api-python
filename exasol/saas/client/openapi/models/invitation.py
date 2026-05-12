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

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.invitation_invitee import InvitationInvitee
    from ..models.invitation_inviter import InvitationInviter
    from ..models.worksheet_connection import WorksheetConnection


T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        id (str):
        organization_id (str):
        inviter (InvitationInviter):
        invitee (InvitationInvitee):
        invitation_url (str):
        created_at (datetime.datetime):
        expires_at (str):
        roles (list[WorksheetConnection]):
        db_username (str):
        databases (list[WorksheetConnection] | Unset):
    """

    id: str
    organization_id: str
    inviter: InvitationInviter
    invitee: InvitationInvitee
    invitation_url: str
    created_at: datetime.datetime
    expires_at: str
    roles: list[WorksheetConnection]
    db_username: str
    databases: list[WorksheetConnection] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization_id = self.organization_id

        inviter = self.inviter.to_dict()

        invitee = self.invitee.to_dict()

        invitation_url = self.invitation_url

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        db_username = self.db_username

        databases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.databases, Unset):
            databases = []
            for databases_item_data in self.databases:
                databases_item = databases_item_data.to_dict()
                databases.append(databases_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "organizationId": organization_id,
                "inviter": inviter,
                "invitee": invitee,
                "invitationUrl": invitation_url,
                "createdAt": created_at,
                "expiresAt": expires_at,
                "roles": roles,
                "dbUsername": db_username,
            }
        )
        if databases is not UNSET:
            field_dict["databases"] = databases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invitation_invitee import InvitationInvitee
        from ..models.invitation_inviter import InvitationInviter
        from ..models.worksheet_connection import WorksheetConnection

        d = dict(src_dict)
        id = d.pop("id")

        organization_id = d.pop("organizationId")

        inviter = InvitationInviter.from_dict(d.pop("inviter"))

        invitee = InvitationInvitee.from_dict(d.pop("invitee"))

        invitation_url = d.pop("invitationUrl")

        created_at = isoparse(d.pop("createdAt"))

        expires_at = d.pop("expiresAt")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = WorksheetConnection.from_dict(roles_item_data)

            roles.append(roles_item)

        db_username = d.pop("dbUsername")

        _databases = d.pop("databases", UNSET)
        databases: list[WorksheetConnection] | Unset = UNSET
        if _databases is not UNSET:
            databases = []
            for databases_item_data in _databases:
                databases_item = WorksheetConnection.from_dict(databases_item_data)

                databases.append(databases_item)

        invitation = cls(
            id=id,
            organization_id=organization_id,
            inviter=inviter,
            invitee=invitee,
            invitation_url=invitation_url,
            created_at=created_at,
            expires_at=expires_at,
            roles=roles,
            db_username=db_username,
            databases=databases,
        )

        return invitation
