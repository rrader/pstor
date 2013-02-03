import os
import sh
from ..helpers import exceptions, pstor
from . import cli_command,inside_pstor

@cli_command
@inside_pstor
def up(**args):
    if pstor.mounted():
        raise exceptions.PstorException("Already up")

    if not args['pass']:
            raise exceptions.PstorException("Choose password with --pass='passwd'")

    cwd = os.getcwd()
    sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
             os.path.join(cwd,'files'),
             extpass="echo '%s'" % args['pass'])