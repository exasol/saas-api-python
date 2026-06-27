from __future__ import annotations

import getpass
import logging
import time
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    Any,
    TypeVar,
    cast,
)

import tenacity
from tenacity.stop import stop_after_delay
from tenacity.wait import wait_fixed

from exasol.saas.client import (
    Limits,
    openapi,
)
from exasol.saas.client._api_access.errors import OpenApiError
from exasol.saas.client.openapi.models import ApiError

LOG = logging.getLogger("exasol.saas.client.api_access")
logging.getLogger("httpx").setLevel(logging.WARNING)

T = TypeVar("T")


def interval_retry(interval: timedelta, timeout: timedelta):
    return tenacity.retry(wait=wait_fixed(interval), stop=stop_after_delay(timeout))


def timestamp_name(project_short_tag: str | None = None) -> str:
    """
    Generates a semi-unique name for a database with the following format:
    - 0-4: number of minutes since the start of the year in hex,
    - 0-5: a semi-random number,
    - provided tag,
    - -username.

    Args:
        project_short_tag: Abbreviation of your project
    """
    now = datetime.now()
    year_start = datetime(now.year, 1, 1)
    minutes_elapsed = int((now - year_start).total_seconds() // 60)
    random_suffix = time.time_ns() % 1048576
    timestamp = f"{minutes_elapsed:05x}{random_suffix:05x}"

    owner = getpass.getuser()
    candidate = f"{timestamp}{project_short_tag or ''}-{owner}"
    return candidate[: Limits.MAX_DATABASE_NAME_LENGTH]


def ensure_type(
    expected: type[T],
    response: T | ApiError | None,
    message: str,
) -> T:
    """
    Ensure the passed response is of the expected type and return it with
    correct type. Otherwise raise an OpenApiError.
    """
    if isinstance(response, expected):
        return cast(T, response)
    api_error = response if isinstance(response, ApiError) else None
    raise OpenApiError(message, api_error)


def _serialize_api_output(response: Any) -> Any:
    if isinstance(response, list):
        return [_serialize_api_output(item) for item in response]

    to_dict = getattr(response, "to_dict", None)
    if callable(to_dict):
        return to_dict()

    return response


def _log_api_output(operation: str, response: Any, **context: Any) -> None:
    if not LOG.isEnabledFor(logging.DEBUG):
        return

    suffix = f" {context}" if context else ""
    LOG.debug(
        "%s response%s: %s",
        operation,
        suffix,
        _serialize_api_output(response),
    )


def _is_not_found(resp: ApiError, entity: str = "User/Database") -> bool:
    return resp.status == 404 and f"{entity} not found" in resp.message


def create_saas_client(
    host: str,
    pat: str,
    raise_on_unexpected_status: bool = True,
) -> openapi.AuthenticatedClient:
    return openapi.AuthenticatedClient(
        base_url=host,
        token=pat,
        raise_on_unexpected_status=raise_on_unexpected_status,
    )
