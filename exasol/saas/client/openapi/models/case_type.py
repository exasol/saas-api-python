from enum import Enum


class CaseType(str, Enum):
    INCIDENT = "incident"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
