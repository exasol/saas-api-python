from datetime import (
    datetime,
    timedelta,
)

import pytest
from tenacity import RetryError

from exasol.saas.client import PROMISING_STATES
from exasol.saas.client.api_access import (
    get_connection_params,
    timestamp_name,
)


@pytest.fixture
def local_name(project_short_tag: str | None) -> str:
    """
    Other than global fixture database_name this fixture uses scope
    "function" to generate an individual name for each test case in this file.
    """
    return timestamp_name(project_short_tag)


@pytest.mark.slow
def test_lifecycle(api_access, local_name):
    """
    This integration test uses the database created and provided by pytest
    context ``_OpenApiAccess.database()`` to verify

    - initial status and number of clusters of the created database
    - list_databases includes the new database
    - delete_database deletes the database
    - list_databases does not include the deleted database anymore
    """

    testee = api_access
    with testee.database(local_name, ignore_delete_failure=True) as db:
        start = datetime.now()
        # verify state and clusters of created database
        assert db.status in PROMISING_STATES and db.clusters.total == 1

        # verify database is listed
        assert db.id in testee.list_database_ids()

        # delete database and verify database is not listed anymore
        testee.delete_database(db.id)
        testee.wait_until_deleted(db.id)
        assert db.id not in testee.list_database_ids()


@pytest.mark.slow
def test_poll(api_access, local_name):
    with api_access.database(local_name) as db:
        with pytest.raises(RetryError):
            api_access.wait_until_running(
                db.id,
                timeout=timedelta(seconds=3),
                interval=timedelta(seconds=1),
            )


@pytest.mark.slow
def test_get_connection(api_access, local_name):
    with api_access.database(local_name) as db:
        clusters = api_access.clusters(db.id)
        connection = api_access.get_connection(db.id, clusters[0].id)
        assert connection.db_username is not None and connection.port == 8563
