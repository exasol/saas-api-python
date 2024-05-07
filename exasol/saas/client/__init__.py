"""
Package openapi contains the API generated from the JSON definition.
"""

from datetime import timedelta
from exasol.saas.client.openapi.models.status import Status


SAAS_HOST = "https://cloud.exasol.com"

# For auto-stopping idle database clusters
MINIMUM_IDLE_TIME = timedelta(minutes=15)

# If deleting a database too early, then logging and accounting could be invalid.
MINIMUM_LIFETIME = timedelta(seconds=30)

PROMISING_STATES = [
    Status.CREATING,
    Status.RUNNING,
    Status.STARTING,
    Status.TOCREATE,
    Status.TOSTART,
]
