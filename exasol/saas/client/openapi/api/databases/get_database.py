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
from ...models.database import Database
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
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}".format(account_id=account_id,database_id=database_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Database]:
    if response.status_code == 200:
        response_200 = Database.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Database]:
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

) -> Response[Database]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Database]
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

) -> Optional[Database]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Database
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

) -> Response[Database]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Database]
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

) -> Optional[Database]:
    """ 
    Args:
        account_id (str):
        database_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Database
     """


    return (await asyncio_detailed(
        account_id=account_id,
database_id=database_id,
client=client,

    )).parsed
