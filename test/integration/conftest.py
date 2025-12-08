import os
from pathlib import Path

import pytest

from exasol.saas.client import openapi
from exasol.saas.client.api_access import (
    OpenApiAccess,
    create_saas_client,
    timestamp_name,
)


def _env(var: str) -> str:
    result = os.environ.get(var)
    if result:
        return result
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
def api_access(saas_host, saas_pat, saas_account_id) -> OpenApiAccess:
    with create_saas_client(saas_host, saas_pat) as client:
        yield OpenApiAccess(client, saas_account_id)


@pytest.fixture(scope="session")
def saas_database(
    api_access, database_name
) -> openapi.models.exasol_database.ExasolDatabase:
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
        yield db.id


@pytest.fixture(scope="session")
def project_short_tag() -> str | None:
    return os.environ.get("PROJECT_SHORT_TAG")


@pytest.fixture(scope="session")
def database_name(project_short_tag) -> str:
    return timestamp_name(project_short_tag)


@pytest.fixture(scope="session")
def allow_connection(api_access) -> None:
    """
    This fixture allows communication with the SaaS from the ci
    for the duration of the test.
    """
    with api_access.allowed_ip():
        yield
