from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """
    Attributes:
        status (float):
        message (str):
        request_id (str):
        path (str):
        method (str):
        timestamp (str):
        causes (Any | Unset):
        log_id (str | Unset):
        handler (str | Unset):
    """

    status: float
    message: str
    request_id: str
    path: str
    method: str
    timestamp: str
    causes: Any | Unset = UNSET
    log_id: str | Unset = UNSET
    handler: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message

        request_id = self.request_id

        path = self.path

        method = self.method

        timestamp = self.timestamp

        causes = self.causes

        log_id = self.log_id

        handler = self.handler

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "message": message,
                "requestId": request_id,
                "path": path,
                "method": method,
                "timestamp": timestamp,
            }
        )
        if causes is not UNSET:
            field_dict["causes"] = causes
        if log_id is not UNSET:
            field_dict["logId"] = log_id
        if handler is not UNSET:
            field_dict["handler"] = handler

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        message = d.pop("message")

        request_id = d.pop("requestId")

        path = d.pop("path")

        method = d.pop("method")

        timestamp = d.pop("timestamp")

        causes = d.pop("causes", UNSET)

        log_id = d.pop("logId", UNSET)

        handler = d.pop("handler", UNSET)

        api_error = cls(
            status=status,
            message=message,
            request_id=request_id,
            path=path,
            method=method,
            timestamp=timestamp,
            causes=causes,
            log_id=log_id,
            handler=handler,
        )

        return api_error
