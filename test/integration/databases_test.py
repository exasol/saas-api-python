import pytest

from exasol.saas.client import openapi, PROMISING_STATES
from tenacity import RetryError
from datetime import datetime, timedelta

from exasol.saas.client.api_access import wait_for_delete_clearance


def test_lifecycle(api_access, database_name):
    """
    This integration test uses the database created and provided by pytest
    context ``_OpenApiAccess.database()`` to verify

    - initial status and number of clusters of the created database
    - list_databases includes the new database
    - delete_database deletes the database
    - list_databases does not include the deleted database anymore
    """

    testee = api_access
    with testee.database(database_name, ignore_delete_failure=True) as db:
        start = datetime.now()
        # verify state and clusters of created database
        assert db.status in PROMISING_STATES and \
            db.clusters.total == 1

        # verify database is listed
        assert db.id in testee.list_database_ids()

        # delete database and verify database is not listed anymore
        wait_for_delete_clearance(start)
        testee.delete_database(db.id)
        assert db.id not in testee.list_database_ids()


def test_poll(api_access, database_name):
    with api_access.database(database_name) as db:
        with pytest.raises(RetryError):
            api_access.wait_until_running(
                db.id,
                timeout=timedelta(seconds=3),
                interval=timedelta(seconds=1),
            )


def test_connect(api_access, database_name):
    with api_access.database(database_name) as db:
        clusters = api_access.clusters(db.id)
        connection = api_access.connect(db.id, clusters[0].id)
        assert connection.db_username is not None and \
            connection.port == 8563
