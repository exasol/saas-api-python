from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    OpenApiError,
    ensure_type,
)
from exasol.saas.client.openapi_facade import ApiError


class MyClass:
    pass


def test_ensure_type_success():
    response = MyClass()
    with not_raises(Exception):
        actual = ensure_type(MyClass, response, "error message")
    assert isinstance(actual, MyClass)


@pytest.mark.parametrize(
    "object, suffix",
    [
        pytest.param(
            ApiError(
                status=400,
                message="inner error",
                request_id="r1",
                path="/path",
                method="GET",
                log_id="l1",
                handler="handler",
                timestamp="now",
            ),
            ": inner error.",
            id="api_error",
        ),
        pytest.param(Mock(), "", id="other_class"),
        pytest.param(None, "", id="none"),
    ],
)
def test_ensure_type_raises_exception(object, suffix):
    prefix = "some error message"
    expected_error = prefix + suffix
    with pytest.raises(OpenApiError, match=expected_error) as ex:
        ensure_type(MyClass, object, prefix)
    assert str(ex.value) == expected_error
