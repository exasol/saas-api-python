from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.allowed_ip import AllowedIP
from ...models.api_error import ApiError
from ...types import Response


def _get_kwargs(
    account_id: str,
    allowlist_ip_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{account_id}/security/allowlist_ip/{allowlist_ip_id}".format(
            account_id=quote(str(account_id), safe=""),
            allowlist_ip_id=quote(str(allowlist_ip_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AllowedIP | ApiError:
    if response.status_code == 200:
        response_200 = AllowedIP.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AllowedIP | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AllowedIP | ApiError]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllowedIP | ApiError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
) -> AllowedIP | ApiError | None:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllowedIP | ApiError
    """

    return sync_detailed(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AllowedIP | ApiError]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllowedIP | ApiError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
) -> AllowedIP | ApiError | None:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllowedIP | ApiError
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            allowlist_ip_id=allowlist_ip_id,
            client=client,
        )
    ).parsed
