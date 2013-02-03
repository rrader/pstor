import sh
from ..helpers import exceptions, pstor
from . import cli_command,inside_pstor

@cli_command
@inside_pstor
def down(**args):
    if not pstor.mounted():
        raise exceptions.PstorException("Already down")

    sh.fusermount('-u', 'files')