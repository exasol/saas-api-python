import os
import nox
from nox import Session
from noxconfig import PROJECT_CONFIG
from exasol.saas.client import SAAS_HOST

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import *

# default actions to be run if nothing is explicitly specified with the -s option
nox.options.sessions = ["fix"]


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
    silent = "CI" in os.environ
    session.run(
        "openapi-python-client",
        "update",
        "--url", f"{SAAS_HOST}/openapi.json",
        "--config", "openapi_config.yml",
        silent=silent,
    )
    session.run("isort", "-q", "exasol/saas/client/openapi")


@nox.session(name="check-api-outdated", python=False)
def check_api_outdated(session: Session):
    """
    Generate API and run git diff to verify if API is out-dated.
    """
    generate_api(session)
    session.run("git", "diff", "--exit-code")
