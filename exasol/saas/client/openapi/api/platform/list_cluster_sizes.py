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
from ...models.cluster_size import ClusterSize
from ...types import (
    UNSET,
    Response,
)


def _get_kwargs(
    platform: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/platforms/{platform}/sizes".format(platform=platform,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List['ClusterSize']]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ClusterSize.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List['ClusterSize']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform: str,
    *,
    client: AuthenticatedClient,

) -> Response[List['ClusterSize']]:
    """ Get cluster sizes for platform

     Get available cluster sizes for platform

    Args:
        platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ClusterSize']]
     """


    kwargs = _get_kwargs(
        platform=platform,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    platform: str,
    *,
    client: AuthenticatedClient,

) -> Optional[List['ClusterSize']]:
    """ Get cluster sizes for platform

     Get available cluster sizes for platform

    Args:
        platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ClusterSize']
     """


    return sync_detailed(
        platform=platform,
client=client,

    ).parsed

async def asyncio_detailed(
    platform: str,
    *,
    client: AuthenticatedClient,

) -> Response[List['ClusterSize']]:
    """ Get cluster sizes for platform

     Get available cluster sizes for platform

    Args:
        platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ClusterSize']]
     """


    kwargs = _get_kwargs(
        platform=platform,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    platform: str,
    *,
    client: AuthenticatedClient,

) -> Optional[List['ClusterSize']]:
    """ Get cluster sizes for platform

     Get available cluster sizes for platform

    Args:
        platform (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ClusterSize']
     """


    return (await asyncio_detailed(
        platform=platform,
client=client,

    )).parsed
