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
from ...models.get_usage_response_200 import GetUsageResponse200
from ...models.get_usage_type import GetUsageType
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    account_id: str,
    *,
    year_month: str,
    type: Union[Unset, GetUsageType] = UNSET,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    params["yearMonth"] = year_month

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{account_id}/usage".format(account_id=account_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GetUsageResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUsageResponse200.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GetUsageResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str,
    type: Union[Unset, GetUsageType] = UNSET,

) -> Response[GetUsageResponse200]:
    """ Get usage

     Show usage for one month

    Args:
        account_id (str):
        year_month (str):
        type (Union[Unset, GetUsageType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsageResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
year_month=year_month,
type=type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str,
    type: Union[Unset, GetUsageType] = UNSET,

) -> Optional[GetUsageResponse200]:
    """ Get usage

     Show usage for one month

    Args:
        account_id (str):
        year_month (str):
        type (Union[Unset, GetUsageType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsageResponse200
     """


    return sync_detailed(
        account_id=account_id,
client=client,
year_month=year_month,
type=type,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str,
    type: Union[Unset, GetUsageType] = UNSET,

) -> Response[GetUsageResponse200]:
    """ Get usage

     Show usage for one month

    Args:
        account_id (str):
        year_month (str):
        type (Union[Unset, GetUsageType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsageResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
year_month=year_month,
type=type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str,
    type: Union[Unset, GetUsageType] = UNSET,

) -> Optional[GetUsageResponse200]:
    """ Get usage

     Show usage for one month

    Args:
        account_id (str):
        year_month (str):
        type (Union[Unset, GetUsageType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsageResponse200
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,
year_month=year_month,
type=type,

    )).parsed
