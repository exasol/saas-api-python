import pytest

from exasol.saas.client import openapi, PROMISING_STATES
from tenacity import RetryError
from datetime import datetime, timedelta

import pyexasol
from exasol.saas.client.api_access import wait_for_delete_clearance, get_connection_params


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


def test_get_connection(api_access, database_name):
    with api_access.database(database_name) as db:
        clusters = api_access.clusters(db.id)
        connection = api_access.get_connection(db.id, clusters[0].id)
        assert connection.db_username is not None and \
            connection.port == 8563


def test_get_connection_params_with_id(saas_host, saas_pat, saas_account_id,
                                       operational_saas_database_id):
    """
    This integration test checks that opening a pyexasol connection to a SaaS DB with
    known id and executing a query works.
    """
    connection_params = get_connection_params(host=saas_host,
                                              account_id=saas_account_id,
                                              pat=saas_pat,
                                              database_id=operational_saas_database_id)
    with pyexasol.connect(**connection_params) as pyconn:
        result = pyconn.execute('SELECT 1;').fetchall()
        assert result == [(1,)]


def test_get_connection_params_with_name(saas_host, saas_pat, saas_account_id,
                                         operational_saas_database_id, database_name):
    """
    This integration test checks that opening a pyexasol connection to a SaaS DB with
    known name and executing a query works.
    """
    connection_params = get_connection_params(host=saas_host,
                                              account_id=saas_account_id,
                                              pat=saas_pat,
                                              database_name=database_name)
    with pyexasol.connect(**connection_params) as pyconn:
        result = pyconn.execute('SELECT 1;').fetchall()
        assert result == [(1,)]
