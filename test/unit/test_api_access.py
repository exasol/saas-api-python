import logging
from datetime import (
    datetime,
    timedelta,
)
from test.util import not_raises
from unittest.mock import Mock

import pytest
from tenacity import TryAgain

from exasol.saas.client.api_access import (
    DatabaseDeleteError,
    DatabaseDeleteTimeout,
    OpenApiAccess,
    OpenApiError,
    _log_api_output,
    ensure_type,
    timestamp_name,
)
from exasol.saas.client.openapi.models.allowed_ip import AllowedIP
from exasol.saas.client.openapi.models.api_error import ApiError
from exasol.saas.client.openapi.models.database_settings import DatabaseSettings
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


def get_database_settings_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import get_database_settings as api

    mock = Mock(side_effect=side_effect)
    monkeypatch.setattr(api, "sync", mock)
    return mock


def list_allowed_ips_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import list_allowed_i_ps as api

    mock = Mock(side_effect=side_effect)
    monkeypatch.setattr(api, "sync", mock)
    return mock


def get_allowed_ip_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import get_allowed_ip as api

    mock = Mock(side_effect=side_effect)
    monkeypatch.setattr(api, "sync", mock)
    return mock


def get_database_mock(monkeypatch, side_effect) -> Mock:
    from exasol.saas.client.api_access import get_database as api

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


def allowed_ip_response(
    id: str = "ip-1",
    *,
    deleted_at=UNSET,
    deleted_by=UNSET,
) -> AllowedIP:
    return AllowedIP(
        id=id,
        name="test-ip",
        cidr_ip="0.0.0.0/0",
        created_at=datetime(2026, 1, 1),
        created_by="tester",
        deleted_at=deleted_at,
        deleted_by=deleted_by,
    )


def database_settings_response(num_nodes: int = 2) -> DatabaseSettings:
    return DatabaseSettings(
        offload_enabled=False,
        auto_updates_enabled=True,
        auto_updates_hard_disabled=False,
        num_nodes=num_nodes,
        stream_type="innovation-release",
        stream_description="Innovation",
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


def test_get_database_settings_retries_transient_not_found(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_settings = get_database_settings_mock(
        monkeypatch,
        [
            api_error(404, "User/Database not found"),
            database_settings_response(),
        ],
    )

    result = api_mock.get_database_settings("db-id")

    assert result is not None
    assert result.num_nodes == 2
    assert get_settings.call_count == 2


def test_get_database_settings_raises_non_retryable_error(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        lambda *_args, **_kwargs: (lambda func: func),
    )
    get_database_settings_mock(
        monkeypatch,
        [api_error(500, "boom")],
    )

    with pytest.raises(OpenApiError, match="Failed to get settings of database db-id"):
        api_mock.get_database_settings("db-id")


def test_log_api_output_serializes_payloads(caplog) -> None:
    caplog.set_level(logging.DEBUG, logger="exasol.saas.client.api_access")

    _log_api_output(
        "list_allowed_i_ps.sync",
        [
            allowed_ip_response("ip-1"),
            ApiError.from_dict({"status": 404, "message": "not found"}),
            None,
        ],
        account_id="A1",
    )

    assert "list_allowed_i_ps.sync response {'account_id': 'A1'}" in caplog.text
    assert "'id': 'ip-1'" in caplog.text
    assert "'status': 404" in caplog.text
    assert "None" in caplog.text


def test_wait_until_allowed_ip_listed_retries(api_mock, monkeypatch) -> None:
    get_allowed_ip_mock(
        monkeypatch,
        [api_error(404, "Item not found"), allowed_ip_response("ip-1")],
    )

    api_mock.wait_until_allowed_ip_listed(
        "ip-1",
        timeout=timedelta(seconds=1),
        interval=timedelta(milliseconds=10),
    )


def test_wait_until_allowed_ip_deleted_retries(api_mock, monkeypatch) -> None:
    get_allowed_ip_mock(
        monkeypatch,
        [
            allowed_ip_response("ip-1"),
            api_error(404, "Item not found"),
        ],
    )

    api_mock.wait_until_allowed_ip_deleted(
        "ip-1",
        timeout=timedelta(seconds=1),
        interval=timedelta(milliseconds=10),
    )


def test_wait_until_allowed_ip_listed_logs_visible_ids(
    api_mock, monkeypatch, caplog
) -> None:
    caplog.set_level(logging.DEBUG, logger="exasol.saas.client.api_access")
    get_allowed_ip_mock(
        monkeypatch,
        [allowed_ip_response("ip-1")],
    )

    api_mock.wait_until_allowed_ip_listed(
        "ip-1",
        timeout=timedelta(seconds=1),
        interval=timedelta(milliseconds=10),
    )

    assert "wait_until_allowed_ip_listed get result" in caplog.text
    assert "get_allowed_ip.sync response" in caplog.text


def test_list_allowed_ip_ids_skips_deleted_entries(api_mock, monkeypatch) -> None:
    list_allowed_ips_mock(
        monkeypatch,
        [
            [
                allowed_ip_response("ip-1"),
                allowed_ip_response(
                    "ip-2",
                    deleted_at=datetime(2026, 1, 2),
                    deleted_by="tester",
                ),
            ]
        ],
    )

    assert list(api_mock.list_allowed_ip_ids()) == ["ip-1"]


def test_wait_until_allowed_ip_deleted_ignores_soft_deleted_entries(
    api_mock, monkeypatch
) -> None:
    get_allowed_ip_mock(
        monkeypatch,
        [
            allowed_ip_response("ip-1"),
            allowed_ip_response(
                "ip-1",
                deleted_at=datetime(2026, 1, 2),
                deleted_by="tester",
            ),
        ],
    )

    api_mock.wait_until_allowed_ip_deleted(
        "ip-1",
        timeout=timedelta(seconds=1),
        interval=timedelta(milliseconds=10),
    )


def test_api_error_from_dict_tolerates_missing_fields() -> None:
    error = ApiError.from_dict(
        {
            "status": 500,
            "message": "boom",
        }
    )

    assert error.status == 500
    assert error.message == "boom"
    assert error.request_id == ""
    assert error.path == ""
    assert error.method == ""
    assert error.log_id == ""
    assert error.handler == ""
    assert error.timestamp == ""
    assert error.causes is UNSET


def test_ensure_type_raises_open_api_error_for_malformed_error_payload() -> None:
    malformed_error = ApiError.from_dict({"message": "backend failed"})

    with pytest.raises(
        OpenApiError,
        match="Failed to do something: backend failed\\.",
    ):
        ensure_type(DatabaseSettings, malformed_error, "Failed to do something")


def test_list_database_ids_skips_deleted_databases(api_mock, monkeypatch) -> None:
    from exasol.saas.client.api_access import list_databases as api

    monkeypatch.setattr(
        api,
        "sync",
        Mock(
            return_value=[
                database_response("active-db"),
                ExasolDatabase(
                    status=Status.DELETING,
                    id="deleted-db-id",
                    name="deleted-db",
                    clusters=ExasolDatabaseClusters(total=1, running=0),
                    provider="aws",
                    region="eu-central-1",
                    created_at=datetime(2026, 1, 1),
                    created_by="tester",
                    deleted_at=datetime(2026, 1, 2),
                    deleted_by="tester",
                ),
                ExasolDatabase(
                    status=Status.TODELETE,
                    id="todelete-db-id",
                    name="todelete-db",
                    clusters=ExasolDatabaseClusters(total=1, running=0),
                    provider="aws",
                    region="eu-central-1",
                    created_at=datetime(2026, 1, 1),
                    created_by="tester",
                ),
            ]
        ),
    )

    assert list(api_mock.list_database_ids()) == ["db-id"]


def test_list_database_ids_logs_visible_ids(api_mock, monkeypatch, caplog) -> None:
    from exasol.saas.client.api_access import list_databases as api

    caplog.set_level(logging.DEBUG, logger="exasol.saas.client.api_access")
    monkeypatch.setattr(
        api,
        "sync",
        Mock(return_value=[database_response("active-db")]),
    )

    assert list(api_mock.list_database_ids()) == ["db-id"]
    assert "list_databases.sync response" in caplog.text
    assert "list_database_ids visible IDs: ['db-id']" in caplog.text


def immediate_retry(*_args, **_kwargs):
    def decorate(func):
        def wrapped():
            for _ in range(5):
                try:
                    return func()
                except TryAgain:
                    pass
                except Exception:
                    raise
            return func()

        return wrapped

    return decorate


def test_wait_until_deleted_uses_get_database_until_not_found(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_database_mock(
        monkeypatch,
        [
            database_response("db-active"),
            ExasolDatabase(
                status=Status.TODELETE,
                id="db-id",
                name="db-active",
                clusters=ExasolDatabaseClusters(total=1, running=0),
                provider="aws",
                region="eu-central-1",
                created_at=datetime(2026, 1, 1),
                created_by="tester",
            ),
            api_error(404, "User/Database not found"),
        ],
    )
    list_databases_mock = Mock(
        side_effect=[
            [database_response("db-active")],
            [],
        ]
    )
    from exasol.saas.client.api_access import list_databases as list_api

    monkeypatch.setattr(list_api, "sync", list_databases_mock)

    api_mock.wait_until_deleted("db-id")


def test_wait_until_deleted_accepts_stale_todelete_when_database_not_listed(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_database_mock(
        monkeypatch,
        [
            ExasolDatabase(
                status=Status.TODELETE,
                id="db-id",
                name="db-active",
                clusters=ExasolDatabaseClusters(total=1, running=0),
                provider="aws",
                region="eu-central-1",
                created_at=datetime(2026, 1, 1),
                created_by="tester",
            )
        ],
    )
    monkeypatch.setattr(
        api_mock,
        "list_database_ids",
        Mock(return_value=iter([])),
    )

    api_mock.wait_until_deleted("db-id")


def test_wait_until_deleted_accepts_todelete_when_helper_list_filters_it(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_database_mock(
        monkeypatch,
        [
            ExasolDatabase(
                status=Status.TODELETE,
                id="db-id",
                name="db-active",
                clusters=ExasolDatabaseClusters(total=1, running=0),
                provider="aws",
                region="eu-central-1",
                created_at=datetime(2026, 1, 1),
                created_by="tester",
            )
        ],
    )
    from exasol.saas.client.api_access import list_databases as api

    monkeypatch.setattr(
        api,
        "sync",
        Mock(
            return_value=[
                ExasolDatabase(
                    status=Status.TODELETE,
                    id="db-id",
                    name="db-active",
                    clusters=ExasolDatabaseClusters(total=1, running=0),
                    provider="aws",
                    region="eu-central-1",
                    created_at=datetime(2026, 1, 1),
                    created_by="tester",
                )
            ]
        ),
    )

    api_mock.wait_until_deleted("db-id")


def test_wait_until_deleted_accepts_soft_deleted_database(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_database_mock(
        monkeypatch,
        [
            ExasolDatabase(
                status=Status.DELETED,
                id="db-id",
                name="db-active",
                clusters=ExasolDatabaseClusters(total=1, running=0),
                provider="aws",
                region="eu-central-1",
                created_at=datetime(2026, 1, 1),
                created_by="tester",
                deleted_at=datetime(2026, 1, 2),
                deleted_by="tester",
            )
        ],
    )

    api_mock.wait_until_deleted("db-id")


def test_wait_until_deleted_retries_when_get_database_returns_none(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        immediate_retry,
    )
    get_database = get_database_mock(
        monkeypatch,
        [
            None,
            api_error(404, "User/Database not found"),
        ],
    )

    api_mock.wait_until_deleted("db-id")

    assert get_database.call_count == 2


def test_wait_until_deleted_times_out_for_active_database(
    api_mock, monkeypatch
) -> None:
    monkeypatch.setattr(
        "exasol.saas.client.api_access.interval_retry",
        lambda *_args, **_kwargs: (lambda func: func),
    )
    monkeypatch.setattr(
        api_mock,
        "list_database_ids",
        Mock(return_value=iter(["db-id"])),
    )
    get_database_mock(
        monkeypatch,
        [database_response("db-active")],
    )

    with pytest.raises(DatabaseDeleteTimeout):
        api_mock.wait_until_deleted("db-id")
