from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    OpenApiError,
    ensure_type,
)
from exasol.saas.client.openapi.models.api_error import ApiError


class MyClass:
    pass


def test_ensure_type_success():
    response = MyClass()
    with not_raises(Exception):
        actual = ensure_type(MyClass, response, "error message")
    assert isinstance(actual, MyClass)


@pytest.mark.parametrize(
    "object",
    [
        Mock(ApiError),
        Mock(),
    ],
)
def test_ensure_type_raises_exception(object):
    with pytest.raises(OpenApiError) as ex:
        ensure_type(MyClass, object, "error message")
    assert ex.api_error
