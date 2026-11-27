from enum import Enum


class AcceptInvitationDatabasesItemPermission(str, Enum):
    ADMIN = "admin"
    READONLY = "readonly"

    def __str__(self) -> str:
        return str(self.value)
