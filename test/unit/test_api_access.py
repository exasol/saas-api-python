from datetime import timedelta
from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    OpenApiAccess,
    indicates_retry,
)
from exasol.saas.client.openapi.errors import UnexpectedStatus

RETRY_EXCEPTION = UnexpectedStatus(
    400, b"Operation is not allowed:The cluster is not in a proper state!"
)


@pytest.mark.parametrize(
    "exception, expected",
    [
        pytest.param(RuntimeError("bla"), False, id="other_exception"),
        pytest.param(UnexpectedStatus(404, b"bla"), False, id="other_status_code"),
        pytest.param(UnexpectedStatus(400, b"bla"), False, id="other_message"),
        pytest.param(RETRY_EXCEPTION, True, id="indicates_retry"),
    ],
)
def test_indicates_retry(exception, expected):
    assert indicates_retry(exception) == expected


class ApiRunner:
    def __init__(self, mocker):
        self.api = OpenApiAccess(Mock(), account_id="A1")
        self._mocker = mocker
        self.mock = None

    def mock_delete(self, side_effect):
        self.mock = Mock(side_effect=side_effect)
        self._mocker.patch(
            "exasol.saas.client.api_access." "delete_database.sync_detailed", self.mock
        )


@pytest.fixture
def api_runner(mocker) -> ApiRunner:
    return ApiRunner(mocker)


@pytest.fixture
def retry_timings() -> dict[str, timedelta]:
    interval = timedelta(seconds=0.2)
    return {
        "min_interval": interval,
        "max_interval": interval,
        "timeout": timedelta(seconds=0.5),
    }


@pytest.mark.parametrize(
    "side_effect",
    [
        pytest.param([UnexpectedStatus(400, b"bla")], id="immediate_failure"),
        pytest.param(
            [RETRY_EXCEPTION, RETRY_EXCEPTION, UnexpectedStatus(400, b"bla")],
            id="failure_after_retry",
        ),
        pytest.param(
            [RETRY_EXCEPTION for _ in range(4)],
            id="timeout_after_too_many_retries",
        ),
    ],
)
def test_delete_fail(side_effect, api_runner, retry_timings) -> None:
    api_runner.mock_delete(side_effect)
    with pytest.raises(UnexpectedStatus):
        api_runner.api.delete_database("123", **retry_timings)


@pytest.mark.parametrize(
    "side_effect, ignore_failures, expected_log_message",
    [
        pytest.param([RETRY_EXCEPTION, None], False, "", id="success"),
        pytest.param(
            [UnexpectedStatus(400, b"bla")],
            True,
            (
                "Ignoring failure when deleting database with"
                " ID 123: Unexpected status code: 400"
            ),
            id="success",
        ),
    ],
)
def test_delete_success(
    side_effect,
    ignore_failures,
    expected_log_message,
    api_runner,
    retry_timings,
    caplog,
) -> None:
    api_runner.mock_delete(side_effect)
    with not_raises(Exception):
        api_runner.api.delete_database(
            database_id="123",
            **retry_timings,
            ignore_failures=ignore_failures,
        )
    assert api_runner.mock.called
    assert expected_log_message in caplog.text
