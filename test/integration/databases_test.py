import logging
import os
from collections import namedtuple
from datetime import datetime

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


@pytest.fixture
def saas_access():
    Access = namedtuple("Access", "client, account_id")
    return Access(
        openapi.AuthenticatedClient(
            base_url=os.environ["SAAS_HOST"],
            token=os.environ["SAAS_PAT"],
        ),
        os.environ["SAAS_ACCOUNT_ID"],
    )


@pytest.fixture
def saas_database(saas_access):
    try:
        cluster_spec = openapi.models.CreateCluster(
            name="my-cluster",
            size="XS",
        )
        response = create_database.sync(
            saas_access.account_id,
            client=saas_access.client,
            body=openapi.models.CreateDatabase(
                name=f"pytest-{timestamp()}",
                initial_cluster=cluster_spec,
                provider="aws",
                region='us-east-1',
            )
        )
        yield response
    finally:
        delete_database.sync_detailed(
            saas_access.account_id,
            response.id,
            client=saas_access.client,
        )


def test_database_lifecycle(saas_access, saas_database):
    """
    This integration test uses the database created and provided by pytest
    fixture ``saas_database`` to verify

    - initial status and number of clusters of the created database
    - list_databases includes the new database
    - delete_database deletes the database
    - list_databases does not include the deleted database anymore
    """
    access = saas_access
    print(f'{os.environ["SAAS_HOST"]}')

    def listed_ids():
        dbs = list_databases.sync(access.account_id, client=access.client)
        return (db.id for db in dbs)

    db = saas_database
    # verify state and clusters of created database
    assert db.status == openapi.models.Status.TOCREATE and \
        db.clusters.total == 1

    # verify database is listed
    assert db.id in listed_ids()

    # delete database and verify database is not listed anymore
    delete_database.sync_detailed(
        access.account_id,
        db.id,
        client=access.client,
    )
    assert db.id not in listed_ids()
