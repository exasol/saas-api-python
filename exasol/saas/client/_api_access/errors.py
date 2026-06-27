from exasol.saas.client.openapi.models import ApiError


class DatabaseStartupFailure(Exception):
    """
    If a SaaS database instance during startup reports a status other than
    successful.
    """


class DatabaseDeleteTimeout(Exception):
    """
    If deletion of a SaaS database instance was requested but during the
    specified timeout it was still reported in the list of existing databases.
    """


class DatabaseDeleteError(Exception):
    """
    Failed to delete a SaaS database instance.
    """


class OpenApiError(Exception):
    def __init__(self, message: str, error: ApiError | None):
        super().__init__(f"{message}: {error.message}." if error else message)


class InternalError(Exception):
    """
    Internal error during delete with retry.
    """
