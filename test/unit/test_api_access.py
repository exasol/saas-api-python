import json
import re
from datetime import timedelta
from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    DatabaseDeleteError,
    OpenApiAccess,
    timestamp_name,
)


def response(status_code: int, message: str):
    json_content = {"message": message}
    return Mock(
        status_code=status_code,
        content=json.dumps(json_content).encode(),
    )


RETRY = response(400, "Operation is not allowed:The cluster is not in a proper state!")


class ApiRunner:
    def __init__(self, monkeypatch):
        self.api = OpenApiAccess(Mock(), account_id="A1")
        self._monkeypatch = monkeypatch
        self.mock = None

    def mock_delete(self, side_effect):
        from exasol.saas.client.api_access import delete_database as api

        self.mock = Mock(side_effect=side_effect)
        self._monkeypatch.setattr(api, "sync_detailed", self.mock)


@pytest.fixture
def api_runner(monkeypatch) -> ApiRunner:
    return ApiRunner(monkeypatch)


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
            [response(400, "bla")],
            id="immediate_failure",
        ),
        pytest.param(
            [RETRY, RETRY, response(400, "bla")],
            id="failure_after_retry",
        ),
        pytest.param(
            [RETRY for _ in range(4)],
            id="timeout_after_too_many_retries",
        ),
    ],
)
def test_delete_fail(api_runner, side_effect, retry_timings) -> None:
    api_runner.mock_delete(side_effect)
    with pytest.raises(DatabaseDeleteError):
        api_runner.api.delete_database("123", **retry_timings)


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
            [response(400, "bla")],
            True,
            ("Ignoring failure when deleting database with ID 123: .*" "Got HTTP 400"),
            id="success_by_ignoring_failures",
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
    assert re.search(expected_log_message, caplog.text, re.MULTILINE)


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
