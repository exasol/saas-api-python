import pytest
import os

from pathlib import Path
from exasol.saas.client import openapi
from api_access import (
    create_saas_client,
    _OpenApiAccess,
    timestamp_name,
)


def _env(var: str) -> str:
    result = os.environ.get(var)
    if not result:
        raise RuntimeError(f"Environment variable {var} is empty.")


@pytest.fixture(scope="session")
def saas_host() -> str:
    return _env("SAAS_HOST")


@pytest.fixture(scope="session")
def saas_pat() -> str:
    return _env("SAAS_PAT")


@pytest.fixture(scope="session")
def saas_account_id() -> str:
    return _env("SAAS_ACCOUNT_ID")


@pytest.fixture(scope="session")
def api_access(saas_host, saas_pat, saas_account_id) -> _OpenApiAccess:
    with create_saas_client(saas_host, saas_pat) as client:
        yield _OpenApiAccess(client, saas_account_id)


@pytest.fixture(scope="session")
def saas_database(api_access, database_name) -> openapi.models.database.Database:
    """
    Note: The SaaS instance database returned by this fixture initially
    will not be operational. The startup takes about 20 minutes.
    """
    with api_access.database(database_name) as db:
        yield db


@pytest.fixture(scope="session")
def operational_saas_database_id(api_access, database_name) -> str:
    with api_access.database(database_name) as db:
        api_access.wait_until_running(db.id)
        yield db


@pytest.fixture(scope="session")
def project_short_tag():
    return os.environ.get("PROJECT_SHORT_TAG")


@pytest.fixture
def database_name(project_short_tag):
    return timestamp_name(project_short_tag)
