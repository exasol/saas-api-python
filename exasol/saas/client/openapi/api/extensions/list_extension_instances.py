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
from ...models.api_error import ApiError
from ...models.extension_instance import ExtensionInstance
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}/extensions/{extension_id}/{extension_version}/instances".format(account_id=account_id,database_id=database_id,extension_id=extension_id,extension_version=extension_version,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiError, List['ExtensionInstance']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ExtensionInstance.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ApiError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiError, List['ExtensionInstance']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ApiError, List['ExtensionInstance']]]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, List['ExtensionInstance']]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
extension_id=extension_id,
extension_version=extension_version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiError, List['ExtensionInstance']]]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, List['ExtensionInstance']]
     """


    return sync_detailed(
        account_id=account_id,
database_id=database_id,
extension_id=extension_id,
extension_version=extension_version,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[ApiError, List['ExtensionInstance']]]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, List['ExtensionInstance']]]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
extension_id=extension_id,
extension_version=extension_version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[ApiError, List['ExtensionInstance']]]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, List['ExtensionInstance']]
     """


    return (await asyncio_detailed(
        account_id=account_id,
database_id=database_id,
extension_id=extension_id,
extension_version=extension_version,
client=client,

    )).parsed
