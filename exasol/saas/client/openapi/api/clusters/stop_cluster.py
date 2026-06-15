from http import HTTPStatus
from typing import (
    Any,
    cast,
)
from urllib.parse import quote

import httpx

from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.actor import Actor
from ...models.api_error import ApiError
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    account_id: str,
    database_id: str,
    cluster_id: str,
    *,
    actor: Actor | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_actor: str | Unset = UNSET
    if not isinstance(actor, Unset):
        json_actor = actor.value

    params["actor"] = json_actor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}/clusters/{cluster_id}/stop".format(
            account_id=quote(str(account_id), safe=""),
            database_id=quote(str(database_id), safe=""),
            cluster_id=quote(str(cluster_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    database_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    actor: Actor | Unset = UNSET,
) -> Response[Any | ApiError]:
    """
    Args:
        account_id (str):
        database_id (str):
        cluster_id (str):
        actor (Actor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        database_id=database_id,
        cluster_id=cluster_id,
        actor=actor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    database_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    actor: Actor | Unset = UNSET,
) -> Any | ApiError | None:
    """
    Args:
        account_id (str):
        database_id (str):
        cluster_id (str):
        actor (Actor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        account_id=account_id,
        database_id=database_id,
        cluster_id=cluster_id,
        client=client,
        actor=actor,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    database_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    actor: Actor | Unset = UNSET,
) -> Response[Any | ApiError]:
    """
    Args:
        account_id (str):
        database_id (str):
        cluster_id (str):
        actor (Actor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        database_id=database_id,
        cluster_id=cluster_id,
        actor=actor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    database_id: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    actor: Actor | Unset = UNSET,
) -> Any | ApiError | None:
    """
    Args:
        account_id (str):
        database_id (str):
        cluster_id (str):
        actor (Actor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            database_id=database_id,
            cluster_id=cluster_id,
            client=client,
            actor=actor,
        )
    ).parsed
