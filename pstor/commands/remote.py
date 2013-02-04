import os
import ConfigParser

from . import cli_command, inside_pstor
from .providers import get_provider_for_url, get_provider_by_name

def args(subparsers):
    remote = subparsers.add_parser('remote')
    remote.add_argument('--list', action="store_true", default=False)
    remote.add_argument('--add', nargs=2)

@cli_command(args=args)
@inside_pstor
def remote(**args):
    if args['list']:
        os.listdir('.pstor/remotes')
    if args['add']:
        name, url = args['add']
        provider = get_provider_for_url(url)
        print "{}: {} => {}".format(name, url, provider.name())
        config = ConfigParser.ConfigParser()
        config.add_section("remote")
        config.set("remote", "name", name)
        config.set("remote", "url", url)
        config.set("remote", "provider", provider.name())

        with file(".pstor/remotes/{}".format(name), "wb") as f:
            config.write(f)