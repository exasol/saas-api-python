""" nox configuration """

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT_DIR = Path(__file__).parent


@dataclass(frozen=True)
class Config:
    """
    Configuration for Nox
    """
    root: Path = ROOT_DIR
    doc: Path = ROOT_DIR / "doc"
    version_file: Path = ROOT_DIR / "version.py"
    path_filters: Iterable[str] = ("dist", ".eggs", "venv")


PROJECT_CONFIG = Config()
