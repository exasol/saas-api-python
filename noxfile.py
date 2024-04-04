""" noxfile """
import nox

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import check # pylint: disable=unused-import

# default actions to be run if nothing is explicitly specified with the -s option
nox.options.sessions = ["fix"]
