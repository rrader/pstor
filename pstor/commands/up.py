import os
import sh
import sys

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

    if not args['pass']:
            raise exceptions.PstorException("Choose password with --pass='passwd'")

    cwd = os.getcwd()
    print "EncFS... ",
    sys.stdout.flush()
    sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
             os.path.join(cwd,'files'),
             extpass="echo '%s'" % args['pass'])
    print "UP"

    for remote in os.listdir('.pstor/remotes'):
        remote = get_remote_by_name(remote)
        print remote.name() + "... ",
        sys.stdout.flush()
        remote.up()
        print "UP"