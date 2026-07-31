from enum import Enum


class McpStatusStatus(str, Enum):
    DISABLED = "disabled"
    DISABLING = "disabling"
    ENABLED = "enabled"
    ENABLING = "enabling"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
