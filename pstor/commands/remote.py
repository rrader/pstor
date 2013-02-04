import os
import urlparse

from . import cli_command, inside_pstor

def args(subparsers):
    remote = subparsers.add_parser('remote')
    remote.add_argument('--list', action="store_true", default=False)
    remote.add_argument('--add')

def get_provider(url):
    if urlparse.urlparse(url).scheme in ['http', 'https']:
        return WebDav

@cli_command(args=args)
@inside_pstor
def remote(**args):
    if args['list']:
        os.listdir('.pstor/remotes')
    if args['add']:
        args['add']
        print urlparse