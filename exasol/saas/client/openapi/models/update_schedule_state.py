from enum import Enum


class UpdateScheduleState(str, Enum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"

    def __str__(self) -> str:
        return str(self.value)
