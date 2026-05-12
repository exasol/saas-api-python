from enum import Enum


class AccountMode(str, Enum):
    PAY_AS_YOU_GO = "pay-as-you-go"
    PRE_PURCHASE = "pre-purchase"
    TRIAL = "trial"

    def __str__(self) -> str:
        return str(self.value)
