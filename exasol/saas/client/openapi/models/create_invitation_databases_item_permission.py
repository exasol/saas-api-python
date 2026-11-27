from enum import Enum


class CreateInvitationDatabasesItemPermission(str, Enum):
    ADMIN = "admin"
    READONLY = "readonly"

    def __str__(self) -> str:
        return str(self.value)
