from typing import Iterable
from contextlib import contextmanager
from datetime import datetime

from exasol.saas.client import openapi
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    list_databases,
)
from exasol.saas.client.openapi.api.security import (
    list_allowed_i_ps,
    add_allowed_ip,
    delete_allowed_ip,
)


def timestamp() -> str:
    return f'{datetime.now().timestamp():.0f}'


def create_saas_client(
        host: str,
        pat: str,
        raise_on_unexpected_status: bool = True,
) -> openapi.AuthenticatedClient:
    return openapi.AuthenticatedClient(
        base_url=host,
        token=pat,
        raise_on_unexpected_status = raise_on_unexpected_status,
    )


class _OpenApiAccess:
    """
    This class is meant to be used only in the context of the API
    generator repository while integration tests in other repositories are
    planned to only use fixture ``saas_database_id()``.
    """

    def __init__(self, client: openapi.Client, account_id: str):
        self._client = client
        self._account_id = account_id

    def create_database(self, cluster_size: str = "XS") -> openapi.models.create_database.CreateDatabase:
        cluster_spec = openapi.models.CreateCluster(
            name="my-cluster",
            size=cluster_size,
        )
        return create_database.sync(
            self._account_id,
            client=self._client,
            body=openapi.models.CreateDatabase(
                name=f"pytest-{timestamp()}",
                initial_cluster=cluster_spec,
                provider="aws",
                region='us-east-1',
            )
        )

    @contextmanager
    def _ignore_failures(self, ignore: bool = False):
        before = self._client.raise_on_unexpected_status
        self._client.raise_on_unexpected_status = not ignore
        yield self._client
        self._client.raise_on_unexpected_status = before

    def delete_database(self, database_id: str, ignore_failures=False):
        with self._ignore_failures(ignore_failures) as client:
            return delete_database.sync_detailed(
                self._account_id, database_id, client=client)

    def list_database_ids(self) -> Iterable[str]:
        dbs = list_databases.sync(self._account_id, client=self._client)
        return (db.id for db in dbs)

    @contextmanager
    def database(
            self,
            keep: bool = False,
            ignore_delete_failure: bool = False,
    ):
        db = None
        try:
            db = self.create_database()
            yield db
        finally:
            if not keep and db:
                self.delete_database(db.id, ignore_delete_failure)
