from enum import Enum


class InvoiceStatus(str, Enum):
    NOT_PAID = "not_paid"
    PAID = "paid"
    PAYMENT_DUE = "payment_due"
    PENDING = "pending"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
