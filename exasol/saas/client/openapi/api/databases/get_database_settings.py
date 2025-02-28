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
from ...models.database_settings import DatabaseSettings
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    database_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}/database_settings".format(account_id=account_id,database_id=database_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DatabaseSettings]:
    if response.status_code == 200:
        response_200 = DatabaseSettings.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DatabaseSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DatabaseSettings]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseSettings]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[DatabaseSettings]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseSettings
     """


    return sync_detailed(
        account_id=account_id,
database_id=database_id,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DatabaseSettings]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabaseSettings]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    database_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[DatabaseSettings]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabaseSettings
     """


    return (await asyncio_detailed(
        account_id=account_id,
database_id=database_id,
client=client,

    )).parsed
