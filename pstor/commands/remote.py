import os
import ConfigParser

from ..helpers import exceptions
from . import cli_command, inside_pstor
from .providers import get_provider_for_url

def args(subparsers):
    remote = subparsers.add_parser('remote')
    remote.add_argument('--list', action="store_true", default=False)
    remote.add_argument('--autoup', action="store_true", default=False)
    remote.add_argument('--add', nargs="+")
    remote.add_argument('--remove')

@cli_command(args=args)
@inside_pstor
def remote(**args):
    if args['list']:
        os.listdir('.pstor/remotes')
    if args['add']:
        name, url = args['add'][:2]

        if os.path.exists(os.path.join('.pstor/remotes', name)):
            raise exceptions.PstorException("Remote with this name already exists")

        provider = get_provider_for_url(url)
        config = ConfigParser.ConfigParser()
        config.add_section("remote")
        config.set("remote", "name", name)
        config.set("remote", "url", url)
        config.set("remote", "autoup", args['autoup'])
        config.set("remote", "provider", provider.name())
        config.set("remote", "options", '\n'.join(args['add']))

        with file(".pstor/remotes/{}".format(name), "wb") as f:
            config.write(f)
        
        print "{} remote '{}' for {} added".format(provider.name(), name, url)

    if args['remove']:
        name = args['remove']
        if not os.path.exists(os.path.join('.pstor/remotes', name)):
            raise exceptions.PstorException("Remote with this name not exists")
        os.remove(os.path.join('.pstor/remotes', name))