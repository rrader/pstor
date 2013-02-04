import os
import sys

from . import cli_command,inside_pstor
from .providers import get_remote_by_name

def args(subparsers):
    subparsers.add_parser('sync')

@cli_command(args=args)
@inside_pstor
def sync(**args):
    for remote in os.listdir('.pstor/remotes'):
        remote = get_remote_by_name(remote)
        print remote.name() + "... ",
        sys.stdout.flush()
        remote.sync()
        print "SYNC"