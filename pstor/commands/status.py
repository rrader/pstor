import os
from ..helpers import exceptions, pstor
from . import cli_command, inside_pstor

@cli_command
@inside_pstor
def status(**args):
    if os.path.isdir(".pstor"):
        if pstor.mounted():
            print "All ok"
        else:
            print "Not mounted. use $ pstor up"
    else:
        raise exceptions.PstorException("Not initialized in this directory. Do\n $ pstor init")