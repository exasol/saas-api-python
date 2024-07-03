import json
import os
import nox
import re
import requests
import shutil
import toml

from datetime import datetime, timezone
from typing import List
from pathlib import Path
from nox import Session
from noxconfig import PROJECT_CONFIG
from exasol.saas.client import SAAS_HOST

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import *

# default actions to be run if nothing is explicitly specified with the -s option
nox.options.sessions = ["fix"]

# destination folder for the generated open api client code
DEST_DIR = "exasol/saas/client/openapi"


def _download_openapi_json() -> Path:
    url = f"{SAAS_HOST}/openapi.json"
    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    content["info"]["download"] = {
        "source": url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    file = Path("openapi.json")
    with open(file, "w") as f:
        json.dump(content, f, indent=4)
    return file


def dependencies(filename: str) -> List[str]:
    def unlimit_max(lib, version):
      version_spec = re.sub(r",.*$", "", version)
      return f"{lib}@{version_spec}"

    with open(filename, "r") as stream:
        _toml = toml.load(stream)
    return [
        unlimit_max(lib, version)
        for lib, version in _toml["tool"]["poetry"]["dependencies"].items()
        if lib != "python"
    ]


@nox.session(name="generate-api", python=False)
def generate_api(session: Session):
    """
    Call openapi-python-client to generate the client api based on the
    openapi specification for Exasol SaaS in JSON format, see
    https://github.com/openapi-generators/openapi-python-client.

    By default run generator silently, Except for CI build, which is detected
    by environment variable ``CI``, see
    https://docs.github.com/en/actions/learn-github-actions/variables.
    #default-environment-variables.
    """
    local_build = "CI" not in os.environ
    filename = _download_openapi_json()
    session.run(
        "openapi-python-client",
        "generate",
        "--path", str(filename),
        "--config", "openapi_config.yml",
        "--output-path", "tmp",
        silent=local_build,
    )
    shutil.rmtree(DEST_DIR)
    shutil.move("tmp/generated", DEST_DIR)
    if local_build:
        session.run("poetry", "add", *dependencies("tmp/pyproject.toml"))
    shutil.rmtree("tmp")
    session.run("isort", "-q", DEST_DIR)


@nox.session(name="check-api-outdated", python=False)
def check_api_outdated(session: Session):
    """
    Generate API and run git diff to verify if API is out-dated.
    """
    generate_api(session)
    session.run("git", "diff", "--exit-code", DEST_DIR)


@nox.session(name="get-project-short-tag", python=False)
def get_project_short_tag(session: Session):
    config_file = Path("error_code_config.yml")
    content = config_file.read_text()
    header = False
    for line in content.splitlines():
        line = line.strip()
        if header:
            print(line.strip().replace(":", ""))
            return
        if line.startswith("error-tags:"):
            header = True
    raise RuntimeError(
        f"Could not read project short tag from file {config_file}"
    )
