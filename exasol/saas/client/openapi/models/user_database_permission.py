from enum import Enum


class UserDatabasePermission(str, Enum):
    ADMIN = "admin"
    READONLY = "readonly"

    def __str__(self) -> str:
        return str(self.value)
