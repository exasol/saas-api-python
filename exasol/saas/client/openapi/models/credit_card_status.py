from enum import Enum


class CreditCardStatus(str, Enum):
    EXPIRED = "expired"
    EXPIRING = "expiring"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
