from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.api_error import ApiError
from ...models.download_file import DownloadFile
from ...types import Response


def _get_kwargs(
    account_id: str,
    database_id: str,
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/internal/accounts/{account_id}/databases/{database_id}/files/{key}".format(
            account_id=quote(str(account_id), safe=""),
            database_id=quote(str(database_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DownloadFile:
    if response.status_code == 200:
        response_200 = DownloadFile.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DownloadFile]:
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
) -> Response[ApiError | DownloadFile]:
    """
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DownloadFile]
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
) -> ApiError | DownloadFile | None:
    """
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DownloadFile
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
) -> Response[ApiError | DownloadFile]:
    """
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DownloadFile]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        database_id=database_id,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    database_id: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | DownloadFile | None:
    """
    Args:
        account_id (str):
        database_id (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DownloadFile
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            database_id=database_id,
            key=key,
            client=client,
        )
    ).parsed
