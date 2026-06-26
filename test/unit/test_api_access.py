from datetime import (
    datetime,
    timedelta,
)
from test.util import not_raises
from unittest.mock import Mock

import pytest

from exasol.saas.client.api_access import (
    DatabaseDeleteError,
    OpenApiAccess,
    timestamp_name,
)
from exasol.saas.client.openapi.models.api_error import ApiError
from exasol.saas.client.openapi.models.exasol_database import ExasolDatabase
from exasol.saas.client.openapi.models.exasol_database_clusters import (
    ExasolDatabaseClusters,
)
from exasol.saas.client.openapi.models.status import Status
from exasol.saas.client.openapi.types import UNSET


def response(status_code: int, message: str, spec=None):
    return Mock(spec, status=status_code, message=message)


def api_error(status_code: int, message: str):
    return response(status_code, message, spec=ApiError)


RETRY = api_error(
    400,
    "Operation is not allowed:The cluster is not in a proper state!",
)


@pytest.fixture
def api_mock():
    return OpenApiAccess(Mock(), account_id="A1")


def delete_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import delete_database as api

    mock = Mock(side_effect=side_effect)
    monkeypatch.setattr(api, "sync", mock)
    return mock


def create_database_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import create_database as api

    mock = Mock(side_effect=side_effect)
    monkeypatch.setattr(api, "sync", mock)
    return mock


def database_response(name: str = "db") -> ExasolDatabase:
    return ExasolDatabase(
        status=Status.CREATING,
        id="db-id",
        name=name,
        clusters=ExasolDatabaseClusters(total=1, running=0),
        provider="aws",
        region="eu-central-1",
        created_at=datetime(2026, 1, 1),
        created_by="tester",
    )


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
def test_delete_fail(api_mock, monkeypatch, side_effect, retry_timings) -> None:
    delete_mock(monkeypatch, side_effect)
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
    monkeypatch,
    retry_timings,
    caplog,
) -> None:
    delete = delete_mock(monkeypatch, side_effect)
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


@pytest.mark.parametrize(
    "num_nodes, expected_num_nodes",
    [
        pytest.param(None, UNSET, id="uses_backend_default"),
        pytest.param(2, 2, id="forwards_explicit_value"),
    ],
)
def test_create_database_num_nodes(
    api_mock, monkeypatch, num_nodes, expected_num_nodes
) -> None:
    create = create_database_mock(
        monkeypatch,
        [database_response("db-with-nodes")],
    )

    result = api_mock.create_database("db-with-nodes", num_nodes=num_nodes)

    assert result is not None
    assert create.called
    body = create.call_args.kwargs["body"]
    assert body.num_nodes == expected_num_nodes


def test_database_context_forwards_num_nodes(api_mock, monkeypatch) -> None:
    create = Mock(return_value=database_response("db-with-context"))
    delete = Mock()
    monkeypatch.setattr(api_mock, "create_database", create)
    monkeypatch.setattr(api_mock, "delete_database", delete)

    with api_mock.database("db-with-context", num_nodes=2) as db:
        assert db is not None
        assert db.name == "db-with-context"

    assert create.call_args.args == ("db-with-context",)
    assert create.call_args.kwargs == {"idle_time": None, "num_nodes": 2}
    delete.assert_called_once_with("db-id", False)
