"""
Package openapi contains the API generated from the JSON definition.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from exasol.saas.client.openapi.models.status import Status


SAAS_HOST = "https://cloud.exasol.com"

PROMISING_STATES = [
    Status.CREATING,
    Status.RUNNING,
    Status.STARTING,
    Status.TOCREATE,
    Status.TOSTART,
]


@dataclass
class Limits:
    """
    Constants for Exasol SaaS databases.
    """
    max_database_name_length: int = 20
    max_cluster_name_length: int = 40
    autostop_min_idle_time: datetime.time = timedelta(minutes=15)
    autostop_max_idle_time: datetime.time = timedelta(minutes=10000)
    autostop_default_idle_time: datetime.time = timedelta(minutes=120)
    # If deleting a database too early, then logging and accounting could be invalid.
    min_database_lifetime: datetime.time = timedelta(seconds=30)


DATABASE_LIMITS = Limits()
