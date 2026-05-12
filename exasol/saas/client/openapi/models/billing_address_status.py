from enum import Enum


class BillingAddressStatus(str, Enum):
    INVALID = "invalid"
    NOT_VALIDATED = "not_validated"
    PARTIALLY_VALID = "partially_valid"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
