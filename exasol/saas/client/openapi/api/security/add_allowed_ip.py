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
from ...models.allowed_ip import AllowedIP
from ...models.create_allowed_ip import CreateAllowedIP
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    account_id: str,
    *,
    body: CreateAllowedIP,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/accounts/{account_id}/security/allowlist_ip".format(account_id=account_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AllowedIP]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AllowedIP.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AllowedIP]:
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
    body: CreateAllowedIP,

) -> Response[AllowedIP]:
    """ Add security rule (CIDR)

     Add security rule to allow access from CIDR

    Args:
        account_id (str):
        body (CreateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllowedIP]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateAllowedIP,

) -> Optional[AllowedIP]:
    """ Add security rule (CIDR)

     Add security rule to allow access from CIDR

    Args:
        account_id (str):
        body (CreateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllowedIP
     """


    return sync_detailed(
        account_id=account_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateAllowedIP,

) -> Response[AllowedIP]:
    """ Add security rule (CIDR)

     Add security rule to allow access from CIDR

    Args:
        account_id (str):
        body (CreateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllowedIP]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateAllowedIP,

) -> Optional[AllowedIP]:
    """ Add security rule (CIDR)

     Add security rule to allow access from CIDR

    Args:
        account_id (str):
        body (CreateAllowedIP):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllowedIP
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,
body=body,

    )).parsed
