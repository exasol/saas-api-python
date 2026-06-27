from __future__ import annotations

from typing import Any

from exasol.saas.client import openapi
from exasol.saas.client._api_access.common import (
    _log_api_output,
    create_saas_client,
    ensure_type,
)
from exasol.saas.client.openapi.api.clusters import (
    get_cluster_connection,
    list_clusters,
)
from exasol.saas.client.openapi.api.databases import list_databases
from exasol.saas.client.openapi.types import UNSET


def _get_database_id(
    account_id: str,
    client: openapi.AuthenticatedClient,
    database_name: str,
) -> str:
    """
    Finds the database id, given the database name.
    """
    dbs = list_databases.sync(account_id, client=client)
    _log_api_output(
        "list_databases.sync",
        dbs,
        account_id=account_id,
        database_name=database_name,
    )
    dbs = list(
        filter(
            lambda db: (db.name == database_name)  # type: ignore
            and (db.deleted_at is UNSET)  # type: ignore
            and (db.deleted_by is UNSET),
            dbs,  # type: ignore
        )
    )  # type: ignore
    if not dbs:
        raise RuntimeError(f"SaaS database {database_name} was not found.")
    return dbs[0].id


def get_database_id(
    host: str,
    account_id: str,
    pat: str,
    database_name: str,
) -> str:
    """
    Finds the database id, given the database name.

    Args:
        host:           SaaS service URL.
        account_id:     User account ID
        pat:            Personal Access Token.
        database_name:  Database name.
    """
    with create_saas_client(host, pat) as client:
        return _get_database_id(account_id, client, database_name)


def get_connection_params(
    host: str,
    account_id: str,
    pat: str,
    database_id: str | None = None,
    database_name: str | None = None,
) -> dict[str, Any]:
    """
    Gets the database connection parameters, such as those required by pyexasol:
    - dns
    - user
    - password.
    Returns the parameters in a dictionary that can be used as kwargs when
    creating a connection, like in the code below:

    connection_params = get_connection_params(...)
    connection = pyexasol.connect(**connection_params)

    Args:
        host:           SaaS service URL.
        account_id:     User account ID
        pat:            Personal Access Token.
        database_id:    Database ID, id known.
        database_name:  Database name, in case the id is unknown.
    """

    with create_saas_client(host, pat) as client:
        if not database_id:
            if not database_name:
                raise ValueError(
                    "To get SaaS connection parameters, "
                    "either database name or database id must be provided."
                )
            database_id = _get_database_id(
                account_id, client, database_name=database_name
            )
        clusters = list_clusters.sync(account_id, database_id, client=client)
        _log_api_output(
            "list_clusters.sync",
            clusters,
            account_id=account_id,
            database_id=database_id,
        )
        cluster_id = next(
            filter(lambda cl: cl.main_cluster, clusters)  # type: ignore
        ).id
        resp = get_cluster_connection.sync(
            account_id, database_id, cluster_id, client=client
        )
        _log_api_output(
            "get_cluster_connection.sync",
            resp,
            account_id=account_id,
            database_id=database_id,
            cluster_id=cluster_id,
        )
        connection = ensure_type(
            openapi.models.ClusterConnection,
            resp,
            "Failed to get the connection data to"
            f" host {host}, account {account_id},"
            f" database with ID {database_id} named {database_name}",
        )
        return {
            "dsn": f"{connection.dns}:{connection.port}",
            "user": connection.db_username,
            "password": pat,
        }
