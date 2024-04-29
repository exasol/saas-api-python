import pytest
import os

from api_access import create_saas_client, _OpenApiAccess


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
    with create_saas_client(saas_host, saas_pat) as client:
        yield _OpenApiAccess(client, saas_account_id)


@pytest.fixture
def saas_database(api_access):
    """
    Note: The SaaS instance database returned by this fixture initially
    will not be operational. The startup takes about 20 minutes.
    """
    with api_access.database() as db:
        yield db
