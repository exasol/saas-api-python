import pytest
import pyexasol
from exasol.saas.client.api_access import get_connection_params


@pytest.mark.slow
def test_get_connection_params_with_id(saas_host, saas_pat, saas_account_id,
                                       operational_saas_database_id,
                                       allow_connection):
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


@pytest.mark.slow
def test_get_connection_params_with_name(saas_host, saas_pat, saas_account_id,
                                         operational_saas_database_id, database_name,
                                         allow_connection):
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


@pytest.mark.slow
def test_xxx():
    print("\ntest case xxx")
