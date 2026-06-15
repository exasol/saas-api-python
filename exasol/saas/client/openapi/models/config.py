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
    from ..models.auth_0 import Auth0
    from ..models.chargebee import Chargebee
    from ..models.config_features import ConfigFeatures
    from ..models.tracking import Tracking


T = TypeVar("T", bound="Config")


@_attrs_define
class Config:
    """
    Attributes:
        signup_url (str):
        pat_url (str):
        recaptcha_key (str):
        features (ConfigFeatures):
        tracking (Tracking | Unset):
        chargebee (Chargebee | Unset):
        auth_0_application (Auth0 | Unset):
        needs_invitation_key (bool | Unset):
    """

    signup_url: str
    pat_url: str
    recaptcha_key: str
    features: ConfigFeatures
    tracking: Tracking | Unset = UNSET
    chargebee: Chargebee | Unset = UNSET
    auth_0_application: Auth0 | Unset = UNSET
    needs_invitation_key: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        signup_url = self.signup_url

        pat_url = self.pat_url

        recaptcha_key = self.recaptcha_key

        features = self.features.to_dict()

        tracking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = self.tracking.to_dict()

        chargebee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chargebee, Unset):
            chargebee = self.chargebee.to_dict()

        auth_0_application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_0_application, Unset):
            auth_0_application = self.auth_0_application.to_dict()

        needs_invitation_key = self.needs_invitation_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "signupUrl": signup_url,
                "patUrl": pat_url,
                "recaptchaKey": recaptcha_key,
                "features": features,
            }
        )
        if tracking is not UNSET:
            field_dict["tracking"] = tracking
        if chargebee is not UNSET:
            field_dict["chargebee"] = chargebee
        if auth_0_application is not UNSET:
            field_dict["auth0Application"] = auth_0_application
        if needs_invitation_key is not UNSET:
            field_dict["needsInvitationKey"] = needs_invitation_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_0 import Auth0
        from ..models.chargebee import Chargebee
        from ..models.config_features import ConfigFeatures
        from ..models.tracking import Tracking

        d = dict(src_dict)
        signup_url = d.pop("signupUrl")

        pat_url = d.pop("patUrl")

        recaptcha_key = d.pop("recaptchaKey")

        features = ConfigFeatures.from_dict(d.pop("features"))

        _tracking = d.pop("tracking", UNSET)
        tracking: Tracking | Unset
        if isinstance(_tracking, Unset):
            tracking = UNSET
        else:
            tracking = Tracking.from_dict(_tracking)

        _chargebee = d.pop("chargebee", UNSET)
        chargebee: Chargebee | Unset
        if isinstance(_chargebee, Unset):
            chargebee = UNSET
        else:
            chargebee = Chargebee.from_dict(_chargebee)

        _auth_0_application = d.pop("auth0Application", UNSET)
        auth_0_application: Auth0 | Unset
        if isinstance(_auth_0_application, Unset):
            auth_0_application = UNSET
        else:
            auth_0_application = Auth0.from_dict(_auth_0_application)

        needs_invitation_key = d.pop("needsInvitationKey", UNSET)

        config = cls(
            signup_url=signup_url,
            pat_url=pat_url,
            recaptcha_key=recaptcha_key,
            features=features,
            tracking=tracking,
            chargebee=chargebee,
            auth_0_application=auth_0_application,
            needs_invitation_key=needs_invitation_key,
        )

        return config
