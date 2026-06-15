from enum import Enum


class InvoiceDunningStatus(str, Enum):
    EXHAUSTED = "exhausted"
    IN_PROGRESS = "in_progress"
    STOPPED = "stopped"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
