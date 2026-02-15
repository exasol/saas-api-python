from pathlib import Path

from exasol.toolbox.config import BaseConfig

PROJECT_CONFIG = BaseConfig(
    root_path=Path(__file__).parent,
    project_name="saas",
    python_versions=("3.10", "3.11", "3.12", "3.13"),
    exasol_versions=("7.1.30",),
    # "exasol/saas/client/openapi/**"
    add_to_excluded_python_paths=("openapi",),
)
