import os
import sh
import shutil
from ..helpers import exceptions
from . import cli_command,inside_pstor

@cli_command
@inside_pstor
def destroy(**args):
    if not os.path.isdir(".pstor"):
        raise exceptions.PstorException("No pstor here")
    else:
        if not args['force']:
            raise exceptions.PstorException("Add --force to confirm")
        sh.fusermount('-u', 'files')
        shutil.rmtree('.pstor')
        shutil.rmtree('files')