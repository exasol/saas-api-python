from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.get_usage_type import GetUsageType
from ...models.usage import Usage
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    account_id: str,
    *,
    year_month: str | Unset = UNSET,
    type_: GetUsageType | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["yearMonth"] = year_month

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{account_id}/usage".format(account_id=quote(str(account_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiError | Usage:
    if response.status_code == 200:
        response_200 = Usage.from_dict(response.json())



        return response_200

    response_default = ApiError.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiError | Usage]:
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
    year_month: str | Unset = UNSET,
    type_: GetUsageType | Unset = UNSET,

) -> Response[ApiError | Usage]:
    """ 
    Args:
        account_id (str):
        year_month (str | Unset):
        type_ (GetUsageType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | Usage]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
year_month=year_month,
type_=type_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str | Unset = UNSET,
    type_: GetUsageType | Unset = UNSET,

) -> ApiError | Usage | None:
    """ 
    Args:
        account_id (str):
        year_month (str | Unset):
        type_ (GetUsageType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | Usage
     """


    return sync_detailed(
        account_id=account_id,
client=client,
year_month=year_month,
type_=type_,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str | Unset = UNSET,
    type_: GetUsageType | Unset = UNSET,

) -> Response[ApiError | Usage]:
    """ 
    Args:
        account_id (str):
        year_month (str | Unset):
        type_ (GetUsageType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | Usage]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
year_month=year_month,
type_=type_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    year_month: str | Unset = UNSET,
    type_: GetUsageType | Unset = UNSET,

) -> ApiError | Usage | None:
    """ 
    Args:
        account_id (str):
        year_month (str | Unset):
        type_ (GetUsageType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | Usage
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,
year_month=year_month,
type_=type_,

    )).parsed
