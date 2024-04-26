import logging
import os
from collections import namedtuple
from datetime import datetime
from contextlib import contextmanager

import pytest

from exasol.saas.client import openapi
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    list_databases,
)

LOG = logging.getLogger(__name__)


def timestamp() -> str:
    return f'{datetime.now().timestamp():.0f}'


def create_saas_access(raise_on_unexpected_status = True):
    Access = namedtuple("Access", "client, account_id")
    return Access(
        openapi.AuthenticatedClient(
            base_url=os.environ["SAAS_HOST"],
            token=os.environ["SAAS_PAT"],
            raise_on_unexpected_status = raise_on_unexpected_status,
        ),
        os.environ["SAAS_ACCOUNT_ID"],
    )


def create_saas_database(saas_access):
    cluster_spec = openapi.models.CreateCluster(
        name="my-cluster",
        size="XS",
    )
    return create_database.sync(
        saas_access.account_id,
        client=saas_access.client,
        body=openapi.models.CreateDatabase(
            name=f"pytest-{timestamp()}",
            initial_cluster=cluster_spec,
            provider="aws",
            region='us-east-1',
        )
    )


def delete_saas_database(saas_access, database_id: str):
    delete_database.sync_detailed(
        saas_access.account_id,
        database_id,
        client=saas_access.client,
    )


@contextmanager
def database_context(
        saas_access,
        keep: bool = False,
        ignore_delete_failure: bool = False,
):
    try:
        db = create_saas_database(saas_access)
        yield db
    finally:
        if not keep:
            access = (create_saas_access(False)
                      if ignore_delete_failure
                      else saas_access)
            delete_saas_database(access, db.id)


@pytest.fixture
def saas_access():
    return create_saas_access()


@pytest.fixture
def saas_database(saas_access):
    with database_context(saas_access, ignore_delete_failure=True) as db:
        yield db


def test_database_list(saas_access, saas_database):
    access = saas_access

    def listed_ids():
        dbs = list_databases.sync(access.account_id, client=access.client)
        return (db.id for db in dbs)

    assert saas_database.id in listed_ids()


def test_database_lifecycle(saas_access):
    """
    This integration test uses the database created and provided by pytest
    fixture ``saas_database`` to verify

    - initial status and number of clusters of the created database
    - list_databases includes the new database
    - delete_database deletes the database
    - list_databases does not include the deleted database anymore
    """
    access = saas_access

    def listed_ids():
        dbs = list_databases.sync(access.account_id, client=access.client)
        return (db.id for db in dbs)

    with database_context(saas_access, ignore_delete_failure=True) as db:
        # verify state and clusters of created database
        assert db.status == openapi.models.Status.TOCREATE and \
            db.clusters.total == 1

        # verify database is listed
        assert db.id in listed_ids()

        # delete database and verify database is not listed anymore
        delete_saas_database(access, db.id)
        assert db.id not in listed_ids()
