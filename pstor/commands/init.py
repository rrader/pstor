import os
import sh
from ..helpers import exceptions
from . import cli_command

@cli_command
def init(**args):
    if os.path.isdir(".pstor"):
        raise exceptions.PstorException("Already initialized.")
    else:
        if not args['pass']:
            raise exceptions.PstorException("Choose password with --pass='passwd'")
        os.mkdir(".pstor")
        os.mkdir(".pstor/remotes")
        os.mkdir(".pstor/encrypted")
        os.mkdir("files")

        cwd = os.getcwd()
        sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
                 os.path.join(cwd,'files'),
                 paranoia=True, extpass="echo '%s'" % args['pass'])

        # sh.cp(sh.glob(os.path.join(cwd,'.pstor/data/*')), cwd, symbolic_link=True, recursive=True)

        print "Now you can add remote for this pstore with\n $ pstor remote add"
