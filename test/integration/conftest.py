import pytest
import os

from api_access import create_saas_client, OpenApiAccess


@pytest.fixture
def saas_host() -> str:
    return os.environ["SAAS_HOST"]


@pytest.fixture
def saas_pat() -> str:
    return os.environ["SAAS_PAT"]


@pytest.fixture
def saas_account_id() -> str:
    return os.environ["SAAS_ACCOUNT_ID"]


@pytest.fixture
def api_access(saas_host, saas_pat, saas_account_id):
    client = create_saas_client(saas_host, saas_pat)
    return OpenApiAccess(client, saas_account_id)


@pytest.fixture
def saas_test_database(api_access):
    with api_access.database() as db:
        yield db

