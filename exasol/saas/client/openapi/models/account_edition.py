from enum import Enum


class AccountEdition(str, Enum):
    ENTERPRISE = "enterprise"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
