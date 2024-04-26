import os
from typing import Iterable, List
from contextlib import contextmanager
from datetime import datetime

from exasol.saas.client import openapi
from exasol.saas.client.openapi.api.databases import (
    create_database,
    delete_database,
    list_databases,
)


def timestamp() -> str:
    return f'{datetime.now().timestamp():.0f}'


class OpenApiTestee:
    def __init__(self):
        self._client = OpenApiTestee.create_client()
        self._account_id = os.environ["SAAS_ACCOUNT_ID"]

    @classmethod
    def create_client(cls, raise_on_unexpected_status: bool = True):
        return openapi.AuthenticatedClient(
            base_url=os.environ["SAAS_HOST"],
            token=os.environ["SAAS_PAT"],
            raise_on_unexpected_status = raise_on_unexpected_status,
        )

    def create_database(self):
        cluster_spec = openapi.models.CreateCluster(
            name="my-cluster",
            size="XS",
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

    def delete_database(self, database_id: str, client=None):
        delete_database.sync_detailed(
            self._account_id,
            database_id,
            client=(client or self._client),
        )

    def list_database_ids(self) -> Iterable[str]:
        dbs = list_databases.sync(self._account_id, client=self._client)
        return (db.id for db in dbs)

    @contextmanager
    def database(
            self,
            keep: bool = False,
            ignore_delete_failure: bool = False,
    ):
        try:
            db = self.create_database()
            yield db
        finally:
            if not keep:
                client = (
                    OpenApiTestee.create_client(False)
                    if ignore_delete_failure
                    else None
                )
                self.delete_database(db.id, client)
