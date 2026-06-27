from __future__ import annotations

from collections.abc import Callable
from datetime import timedelta
from typing import cast

from tenacity import TryAgain

from exasol.saas.client import openapi
from exasol.saas.client._api_access.common import (
    LOG,
    _log_api_output,
    ensure_type,
    interval_retry,
    timestamp_name,
)
from exasol.saas.client.openapi.api.security import (
    add_allowed_ip,
    list_allowed_i_ps,
)
from exasol.saas.client.openapi.models import ApiError
from exasol.saas.client.openapi.types import UNSET


def _build_allowed_ip_rule(cidr_ip: str) -> openapi.models.CreateAllowedIP:
    return openapi.models.CreateAllowedIP(
        name=timestamp_name(),
        cidr_ip=cidr_ip,
    )


def _is_active_allowed_ip(
    allowed_ip: openapi.models.AllowedIP | ApiError | None,
) -> bool:
    if allowed_ip is None or isinstance(allowed_ip, ApiError):
        return False
    return allowed_ip.deleted_at is UNSET and allowed_ip.deleted_by is UNSET


def _list_active_allowed_ip_ids(
    account_id: str,
    client: openapi.AuthenticatedClient,
) -> list[str]:
    resp = list_allowed_i_ps.sync(account_id, client=client) or []
    _log_api_output(
        "list_allowed_i_ps.sync",
        resp,
        account_id=account_id,
    )
    ips = ensure_type(list, resp, "Failed to retrieve the list of allowed ips")
    visible_allowed_ip_ids = [
        ip.id for ip in ips if ip.deleted_at is UNSET and ip.deleted_by is UNSET
    ]
    LOG.debug("list_allowed_ip_ids visible IDs: %s", visible_allowed_ip_ids)
    return visible_allowed_ip_ids


def _resolve_active_allowed_ip(
    allowed_ip_id: str,
    get_allowed_ip_by_id: Callable[[str], openapi.models.AllowedIP | ApiError | None],
    timeout: timedelta,
    interval: timedelta,
) -> openapi.models.AllowedIP:
    @interval_retry(interval, timeout)
    def resolve() -> openapi.models.AllowedIP:
        LOG.debug(
            "wait_until_allowed_ip_listed state {'allowed_ip_id': %s}",
            allowed_ip_id,
        )
        allowed_ip = get_allowed_ip_by_id(allowed_ip_id)
        if _is_active_allowed_ip(allowed_ip):
            return cast(openapi.models.AllowedIP, allowed_ip)
        raise TryAgain

    return resolve()


def _wait_until_allowed_ip_deleted(
    allowed_ip_id: str,
    get_allowed_ip_by_id: Callable[[str], openapi.models.AllowedIP | ApiError | None],
    timeout: timedelta,
    interval: timedelta,
) -> None:
    @interval_retry(interval, timeout)
    def verify_deleted() -> bool:
        LOG.debug(
            "wait_until_allowed_ip_deleted state {'allowed_ip_id': %s}",
            allowed_ip_id,
        )
        allowed_ip = get_allowed_ip_by_id(allowed_ip_id)
        if _is_active_allowed_ip(allowed_ip):
            raise TryAgain
        return True

    verify_deleted()


def _add_allowed_ip(
    account_id: str,
    client: openapi.AuthenticatedClient,
    cidr_ip: str,
    get_allowed_ip_by_id: Callable[[str], openapi.models.AllowedIP | ApiError | None],
) -> openapi.models.AllowedIP:
    resp = add_allowed_ip.sync(
        account_id,
        client=client,
        body=_build_allowed_ip_rule(cidr_ip),
    )
    _log_api_output(
        "add_allowed_ip.sync",
        resp,
        account_id=account_id,
        cidr_ip=cidr_ip,
    )
    created_ip = ensure_type(
        openapi.models.AllowedIP,
        resp,
        f"Failed to add allowed IP address {cidr_ip}",
    )
    return _resolve_active_allowed_ip(
        created_ip.id,
        get_allowed_ip_by_id=get_allowed_ip_by_id,
        timeout=timedelta(minutes=6),
        interval=timedelta(seconds=5),
    )
