import os
from ..helpers import exceptions, pstor
from . import cli_command, inside_pstor

def args(subparsers):
    subparsers.add_parser('status')

@cli_command(args=args)
@inside_pstor
def status(**args):
    if pstor.mounted():
        print "All ok"
    else:
        print "Not mounted. use $ pstor up"