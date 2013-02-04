import os
import sh
import sys
import getpass

from ..helpers import exceptions, pstor
from . import cli_command,inside_pstor
from .providers import get_remote_by_name

def args(subparsers):
    up = subparsers.add_parser('up')
    up.add_argument('--pass')

@cli_command(args=args)
@inside_pstor
def up(**args):
    if pstor.mounted():
        raise exceptions.PstorException("Already up")

    password = args['pass']
    if not password:
        password = getpass.getpass()

    for remote in os.listdir('.pstor/remotes'):
        remote = get_remote_by_name(remote)
        print remote.name() + "... ",
        sys.stdout.flush()
        remote.up()
        print "UP"

    cwd = os.getcwd()
    print "EncFS... ",
    sys.stdout.flush()
    sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
             os.path.join(cwd,'files'),
             extpass="echo '%s'" % password)
    print "UP"