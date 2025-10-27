from enum import Enum


class ScheduleState(str, Enum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"

    def __str__(self) -> str:
        return str(self.value)
