import os
import sh
from time import sleep
import getpass

from ..helpers import exceptions
from . import cli_command

def args(subparsers):
    init = subparsers.add_parser('init')
    init.add_argument('--pass')
    init.add_argument('--exists', action="store_true", default=False)

@cli_command(args=args)
def init(**args):
    if os.path.isdir(".pstor"):
        raise exceptions.PstorException("Already initialized.")
    else:
        password = args['pass']
        if not password and not args['exists']:
            password = getpass.getpass()

        os.mkdir(".pstor")
        os.mkdir(".pstor/remotes")
        os.mkdir(".pstor/encrypted")
        os.mkdir("files")

        cwd = os.getcwd()
        if not args['exists']:
            sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
                     os.path.join(cwd,'files'),
                     paranoia=True, extpass="echo '%s'" % password)
            sleep(1)
            sh.fusermount('-u', 'files')

        # sh.cp(sh.glob(os.path.join(cwd,'.pstor/data/*')), cwd, symbolic_link=True, recursive=True)

        print "Now you can add remote for this pstore with\n $ pstor remote --add"
