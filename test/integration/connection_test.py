import contextlib
import ssl

import pyexasol
import pytest

from exasol.saas.client.api_access import get_connection_params

SSL_OPTIONS = {"websocket_sslopt": {"cert_reqs": ssl.CERT_NONE}}


@pytest.fixture
def pyexasol_connection(
    saas_host,
    saas_pat,
    saas_account_id,
    allow_connection,
    operational_saas_database_id,
):
    @contextlib.contextmanager
    def connect(**kwargs):
        params = get_connection_params(
            host=saas_host,
            account_id=saas_account_id,
            pat=saas_pat,
            **kwargs,
        )
        params.update(SSL_OPTIONS)
        with pyexasol.connect(**params) as con:
            yield con

    return connect


@pytest.mark.slow
def test_get_connection_params_with_id(
    pyexasol_connection,
    operational_saas_database_id,
):
    """
    This integration test checks that opening a pyexasol connection to a SaaS DB with
    known id and executing a query works.
    """
    with pyexasol_connection(database_id=operational_saas_database_id) as pyconn:
        result = pyconn.execute("SELECT 1;").fetchall()
        assert result == [(1,)]


@pytest.mark.slow
def test_get_connection_params_with_name(pyexasol_connection, database_name):
    """
    This integration test checks that opening a pyexasol connection to a SaaS DB with
    known name and executing a query works.
    """
    with pyexasol_connection(database_name=database_name) as pyconn:
        result = pyconn.execute("SELECT 1;").fetchall()
        assert result == [(1,)]
