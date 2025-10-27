from http import HTTPStatus
from typing import (
    Any,
    Optional,
    Union,
    cast,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.api_error import ApiError
from ...models.update_allowed_ip import UpdateAllowedIP
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    allowlist_ip_id: str,
    *,
    body: UpdateAllowedIP,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/accounts/{account_id}/security/allowlist_ip/{allowlist_ip_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, ApiError]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiError]]:
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
    body: UpdateAllowedIP,
) -> Response[Union[Any, ApiError]]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):
        body (UpdateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
        body=body,
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
    body: UpdateAllowedIP,
) -> Optional[Union[Any, ApiError]]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):
        body (UpdateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiError]
    """

    return sync_detailed(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllowedIP,
) -> Response[Union[Any, ApiError]]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):
        body (UpdateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiError]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        allowlist_ip_id=allowlist_ip_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    allowlist_ip_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllowedIP,
) -> Optional[Union[Any, ApiError]]:
    """
    Args:
        account_id (str):
        allowlist_ip_id (str):
        body (UpdateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiError]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            allowlist_ip_id=allowlist_ip_id,
            client=client,
            body=body,
        )
    ).parsed
