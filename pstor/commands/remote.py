import os

from . import cli_command, inside_pstor
from .providers import get_provider

def args(subparsers):
    remote = subparsers.add_parser('remote')
    remote.add_argument('--list', action="store_true", default=False)
    remote.add_argument('--add')

@cli_command(args=args)
@inside_pstor
def remote(**args):
    if args['list']:
        os.listdir('.pstor/remotes')
    if args['add']:
        print get_provider(args['add'])