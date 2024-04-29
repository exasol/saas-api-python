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
from exasol.saas.client.openapi.api.security import (
    list_allowed_i_ps,
    add_allowed_ip,
    delete_allowed_ip,
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

    def _get_client(self, ignore_failures: bool = False):
        return (
            OpenApiTestee.create_client(False)
            if ignore_failures
            else self._client
        )

    def create_database(self) -> openapi.models.create_database.CreateDatabase:
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

    def delete_database(self, database_id: str, ignore_failures=False):
        return delete_database.sync_detailed(
            self._account_id,
            database_id,
            client=self._get_client(ignore_failures),
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
                self.delete_database( db.id, ignore_delete_failure)

    def list_allowed_ip_ids(self) -> Iterable[openapi.models.allowed_ip.AllowedIP]:
        ips = list_allowed_i_ps.sync(
            self._account_id,
            client=self._client,
        )
        return (x.id for x in ips)

    def add_allowed_ip(self, cidr_ip: str = "0.0.0.0/0") -> openapi.models.allowed_ip.AllowedIP:
        """
        Suggested values for cidr_ip:
        * 185.17.207.78/32
        * 0.0.0.0/0 = all ipv4
        * ::/0 = all ipv6
        """
        rule = openapi.models.create_allowed_ip.CreateAllowedIP(
            name=f"pytest-{timestamp()}",
            cidr_ip=cidr_ip,
        )
        return add_allowed_ip.sync(
            self._account_id,
            client=self._client,
            body=rule,
        )

    def delete_allowed_ip(self, id: str, ignore_failures=False):
        return delete_allowed_ip.sync_detailed(
            self._account_id,
            id,
            client=self._get_client(ignore_failures),
        )

    @contextmanager
    def allowed_ip(
            self,
            cidr_ip: str = "0.0.0.0/0",
            keep: bool = False,
            ignore_delete_failure: bool = False,
    ):
        try:
            ip = self.add_allowed_ip(cidr_ip)
            yield ip
        finally:
            if not keep:
                self.delete_allowed_ip(id, ignore_delete_failure)
