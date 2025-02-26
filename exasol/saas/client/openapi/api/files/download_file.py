from http import HTTPStatus
from typing import (
    Any,
    Dict,
    List,
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
from ...models.download_file import DownloadFile
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    database_id: str,
    key: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/internal/accounts/{account_id}/databases/{database_id}/files/{key}".format(account_id=account_id,database_id=database_id,key=key,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DownloadFile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DownloadFile.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DownloadFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    database_id: str,
    key: str,
    *,
    client: AuthenticatedClient,

) -> Response[DownloadFile]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadFile]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
key=key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    database_id: str,
    key: str,
    *,
    client: AuthenticatedClient,

) -> Optional[DownloadFile]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadFile
     """


    return sync_detailed(
        account_id=account_id,
database_id=database_id,
key=key,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    database_id: str,
    key: str,
    *,
    client: AuthenticatedClient,

) -> Response[DownloadFile]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadFile]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
key=key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    database_id: str,
    key: str,
    *,
    client: AuthenticatedClient,

) -> Optional[DownloadFile]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadFile
     """


    return (await asyncio_detailed(
        account_id=account_id,
database_id=database_id,
key=key,
client=client,

    )).parsed
