from enum import Enum


class Scope(str, Enum):
    BILLINGREAD = "billing:read"
    BILLINGWRITE = "billing:write"
    DATABASESOPERATE = "databases:operate"
    DATABASESUSE = "databases:use"
    FILEMANAGEWRITE = "filemanage:write"
    INTEGRATIONSWRITE = "integrations:write"
    MONITORINGREAD = "monitoring:read"
    SECURITYREAD = "security:read"
    SECURITYWRITE = "security:write"
    USERSREAD = "users:read"
    USERSWRITE = "users:write"

    def __str__(self) -> str:
        return str(self.value)
