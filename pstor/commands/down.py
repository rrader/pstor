import sh
from ..helpers import exceptions, pstor
from . import cli_command,inside_pstor

def args(subparsers):
    subparsers.add_parser('down')

@cli_command(args=args)
@inside_pstor
def down(**args):
    if not pstor.mounted():
        raise exceptions.PstorException("Already down")

    sh.fusermount('-u', 'files')