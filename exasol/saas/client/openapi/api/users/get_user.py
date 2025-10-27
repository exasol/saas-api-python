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
from ...models.user import User
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/internal/accounts/{account_id}/users/{user_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ApiError, User]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiError, User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiError, User]]:
    """
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, User]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiError, User]]:
    """
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, User]
    """

    return sync_detailed(
        account_id=account_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiError, User]]:
    """
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, User]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiError, User]]:
    """
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, User]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
