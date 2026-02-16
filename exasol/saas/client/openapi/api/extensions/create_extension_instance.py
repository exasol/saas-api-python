from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.api_error import ApiError
from ...models.create_extension_instance import CreateExtensionInstance
from ...models.extension_instance import ExtensionInstance
from ...types import Response


def _get_kwargs(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    body: CreateExtensionInstance,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/accounts/{account_id}/databases/{database_id}/extensions/{extension_id}/{extension_version}/instances".format(
            account_id=quote(str(account_id), safe=""),
            database_id=quote(str(database_id), safe=""),
            extension_id=quote(str(extension_id), safe=""),
            extension_version=quote(str(extension_version), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ExtensionInstance:
    if response.status_code == 200:
        response_200 = ExtensionInstance.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ApiError.from_dict(response.json())

        return response_422

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | ExtensionInstance]:
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
    body: CreateExtensionInstance,
) -> Response[ApiError | ExtensionInstance]:
    """
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):
        body (CreateExtensionInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ExtensionInstance]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        database_id=database_id,
        extension_id=extension_id,
        extension_version=extension_version,
        body=body,
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
    body: CreateExtensionInstance,
) -> ApiError | ExtensionInstance | None:
    """
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):
        body (CreateExtensionInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ExtensionInstance
    """

    return sync_detailed(
        account_id=account_id,
        database_id=database_id,
        extension_id=extension_id,
        extension_version=extension_version,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,
    body: CreateExtensionInstance,
) -> Response[ApiError | ExtensionInstance]:
    """
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):
        body (CreateExtensionInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ExtensionInstance]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        database_id=database_id,
        extension_id=extension_id,
        extension_version=extension_version,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    database_id: str,
    extension_id: str,
    extension_version: str,
    *,
    client: AuthenticatedClient,
    body: CreateExtensionInstance,
) -> ApiError | ExtensionInstance | None:
    """
    Args:
        account_id (str):
        database_id (str):
        extension_id (str):
        extension_version (str):
        body (CreateExtensionInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ExtensionInstance
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            database_id=database_id,
            extension_id=extension_id,
            extension_version=extension_version,
            client=client,
            body=body,
        )
    ).parsed
