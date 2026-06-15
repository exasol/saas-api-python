from enum import Enum


class RegisterSignupPath(str, Enum):
    LAKEHOUSE_TURBO_SIGNUP = "lakehouse-turbo-signup"
    SIGNUP = "signup"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
