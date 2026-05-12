from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebsocketConfig")


@_attrs_define
class WebsocketConfig:
    """
    Attributes:
        ws_ticket (str):
    """

    ws_ticket: str

    def to_dict(self) -> dict[str, Any]:
        ws_ticket = self.ws_ticket

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "wsTicket": ws_ticket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ws_ticket = d.pop("wsTicket")

        websocket_config = cls(
            ws_ticket=ws_ticket,
        )

        return websocket_config
