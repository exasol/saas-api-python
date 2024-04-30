import pytest
import os

from exasol.saas.client import openapi
from api_access import create_saas_client, _OpenApiAccess

@pytest.fixture(scope="session")
def saas_host() -> str:
    return os.environ["SAAS_HOST"]


@pytest.fixture(scope="session")
def saas_pat() -> str:
    return os.environ["SAAS_PAT"]


@pytest.fixture(scope="session")
def saas_account_id() -> str:
    return os.environ["SAAS_ACCOUNT_ID"]


@pytest.fixture(scope="session")
def api_access(saas_host, saas_pat, saas_account_id) -> _OpenApiAccess:
    with create_saas_client(saas_host, saas_pat) as client:
        yield _OpenApiAccess(client, saas_account_id)


@pytest.fixture(scope="session")
def saas_database(api_access) -> openapi.models.database.Database:
    """
    Note: The SaaS instance database returned by this fixture initially
    will not be operational. The startup takes about 20 minutes.
    """
    with api_access.database() as db:
        yield db


@pytest.fixture(scope="session")
def operational_saas_database_id(api_access) -> str:
    with api_access.database() as db:
        api_access.wait_until_running(db.id)
        yield db
