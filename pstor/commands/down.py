import os
import sys
import sh

from ..helpers import pstor
from . import cli_command,inside_pstor
from .providers import get_remote_by_name
from . import sync

def args(subparsers):
    down = subparsers.add_parser('down')
    down.add_argument('--force', action="store_true", default=False)

@cli_command(args=args)
@inside_pstor
def down(**args):
    if not args['force']:
        print "Sync before down..."
        sync.sync(**args)

    for remote in os.listdir('.pstor/remotes'):
        remote = get_remote_by_name(remote)
        print remote.name() + "... ",
        sys.stdout.flush()
        remote.down()
        print "DOWN"

    if not pstor.mounted():
        print "Already down"

    print "EncFS... ",
    sys.stdout.flush()
    pstor.umount('files')
    print "DOWN"