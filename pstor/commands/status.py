import os
import sh
from ..helpers import exceptions
from . import cli_command

@cli_command
def status(**args):
    if os.path.isdir(".pstor"):
        cwd = os.path.join(os.getcwd(), 'files')
        if any(cwd == path.strip() for path in 
            list(sh.awk(sh.grep(sh.mount(), 'encfs'), "{print $3}"))):
            print "All ok"
    else:
        raise exceptions.PstorException("Not initialized in this directory. Do\n $ pstor init")