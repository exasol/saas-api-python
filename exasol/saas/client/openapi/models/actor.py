from enum import Enum


class Actor(str, Enum):
    AUTO_STOP = "auto-stop"
    SCHEDULED_ACTION = "scheduled-action"

    def __str__(self) -> str:
        return str(self.value)
