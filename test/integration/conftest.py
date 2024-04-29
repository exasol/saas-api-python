import pytest

from api_testee import OpenApiTestee


@pytest.fixture
def api_testee():
    return OpenApiTestee()
