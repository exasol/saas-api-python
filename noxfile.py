import nox
from nox import Session
from noxconfig import PROJECT_CONFIG

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
    """
    session.run(
        "openapi-python-client",
        "update",
        "--url", "https://cloud.exasol.com/openapi.json",
        "--config", "openapi_config.yml",
    )
    session.run("isort", "-q", "exasol/saas/client/openapi")
