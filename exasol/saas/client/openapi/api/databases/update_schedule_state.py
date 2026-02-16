from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_error import ApiError
from ...models.update_schedule_state import UpdateScheduleState
from typing import cast



def _get_kwargs(
    account_id: str,
    database_id: str,
    action_id: str,
    *,
    body: UpdateScheduleState,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}/schedules/{action_id}/state".format(account_id=quote(str(account_id), safe=""),database_id=quote(str(database_id), safe=""),action_id=quote(str(action_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ApiError:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = ApiError.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    database_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateScheduleState,

) -> Response[Any | ApiError]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        action_id (str):
        body (UpdateScheduleState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
action_id=action_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: str,
    database_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateScheduleState,

) -> Any | ApiError | None:
    """ 
    Args:
        account_id (str):
        database_id (str):
        action_id (str):
        body (UpdateScheduleState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
     """


    return sync_detailed(
        account_id=account_id,
database_id=database_id,
action_id=action_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_id: str,
    database_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateScheduleState,

) -> Response[Any | ApiError]:
    """ 
    Args:
        account_id (str):
        database_id (str):
        action_id (str):
        body (UpdateScheduleState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
database_id=database_id,
action_id=action_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: str,
    database_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateScheduleState,

) -> Any | ApiError | None:
    """ 
    Args:
        account_id (str):
        database_id (str):
        action_id (str):
        body (UpdateScheduleState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
     """


    return (await asyncio_detailed(
        account_id=account_id,
database_id=database_id,
action_id=action_id,
client=client,
body=body,

    )).parsed
