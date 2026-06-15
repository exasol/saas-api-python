from enum import Enum


class CasePriority(str, Enum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
