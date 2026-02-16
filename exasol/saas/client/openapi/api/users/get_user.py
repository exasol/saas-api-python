from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.user import User
from typing import cast



def _get_kwargs(
    account_id: str,
    user_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/internal/accounts/{account_id}/users/{user_id}".format(account_id=quote(str(account_id), safe=""),user_id=quote(str(user_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | User:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())



        return response_200

    response_default = ApiError.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | User]:
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

) -> Response[ApiError | User]:
    """ 
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | User]
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

) -> ApiError | User | None:
    """ 
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | User
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

) -> Response[ApiError | User]:
    """ 
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | User]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
user_id=user_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,

) -> ApiError | User | None:
    """ 
    Args:
        account_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | User
     """


    return (await asyncio_detailed(
        account_id=account_id,
user_id=user_id,
client=client,

    )).parsed
