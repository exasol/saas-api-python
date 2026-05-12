from enum import Enum


class InvoicePriceType(str, Enum):
    TAX_EXCLUSIVE = "tax_exclusive"
    TAX_INCLUSIVE = "tax_inclusive"

    def __str__(self) -> str:
        return str(self.value)
