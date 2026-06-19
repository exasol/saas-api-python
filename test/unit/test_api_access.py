from datetime import timedelta
from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    DatabaseDeleteError,
    OpenApiAccess,
    create_saas_client,
    timestamp_name,
)
from exasol.saas.client.openapi_facade import (
    ApiError,
    OpenApiFacade,
)


def response(status_code: int, message: str, spec=None):
    return Mock(spec, status=status_code, message=message)


def api_error(status_code: int, message: str):
    return ApiError(
        status=status_code,
        message=message,
        request_id="r1",
        path="/path",
        method="DELETE",
        log_id="l1",
        handler="handler",
        timestamp="now",
    )


RETRY = api_error(
    400,
    "Operation is not allowed:The cluster is not in a proper state!",
)


@pytest.fixture
def api_mock():
    return OpenApiAccess(Mock(), account_id="A1")


def delete_mock(api_mock, side_effect) -> Mock:
    mock = Mock(side_effect=side_effect)
    api_mock._client.delete_database = mock
    return mock


@pytest.fixture
def retry_timings() -> dict[str, timedelta]:
    """
    Common timings, used by some of the test cases in this file.
    """
    interval = timedelta(seconds=0.2)
    return {
        "min_interval": interval,
        "max_interval": interval,
        "timeout": timedelta(seconds=0.5),
    }


@pytest.mark.parametrize(
    "side_effect",
    [
        pytest.param(
            [api_error(400, "bla")],
            id="immediate_failure",
        ),
        pytest.param(
            [RETRY, RETRY, api_error(400, "bla")],
            id="failure_after_retry",
        ),
        pytest.param(
            [RETRY for _ in range(4)],
            id="timeout_after_too_many_retries",
        ),
    ],
)
def test_delete_fail(api_mock, side_effect, retry_timings) -> None:
    delete_mock(api_mock, side_effect)
    with pytest.raises(DatabaseDeleteError):
        api_mock.delete_database("123", **retry_timings)


@pytest.mark.parametrize(
    "side_effect, ignore_failures, expected_log_message",
    [
        pytest.param(
            [RETRY, response(200, "")],
            False,
            "",
            id="success_after_retry",
        ),
        pytest.param(
            [api_error(400, "bla")],
            True,
            "Ignoring delete failure: HTTP 400:",
            id="success_by_ignoring_failures",
        ),
    ],
)
def test_delete_success(
    side_effect,
    ignore_failures,
    expected_log_message,
    api_mock,
    retry_timings,
    caplog,
) -> None:
    delete = delete_mock(api_mock, side_effect)
    with not_raises(Exception):
        api_mock.delete_database(
            database_id="123",
            **retry_timings,
            ignore_failures=ignore_failures,
        )
    assert delete.called
    assert expected_log_message in caplog.text


def test_timestamp_name() -> None:
    names = [timestamp_name("TEST") for _ in range(3)]
    minutes = [int(name[:5], 16) for name in names]
    suffixes = [int(name[5:10], 16) for name in names]
    tags = [name[10:14] for name in names]
    # minutes from the start of the year should be the same
    assert minutes[0] == minutes[1] or minutes[1] == minutes[2]
    # suffixes should all be different
    assert len(set(suffixes)) == 3
    # the provided tag should follow the hacky timestamp.
    assert all(tag == "TEST" for tag in tags)


def test_create_saas_client_returns_facade() -> None:
    client = create_saas_client("https://example.org", "pat")
    assert isinstance(client, OpenApiFacade)
