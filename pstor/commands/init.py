import os
import sh
from ..helpers import exceptions

def init(**args):
    if os.path.isdir(".pstor"):
        raise exceptions.PstorException("Already initialized.")
    else:
        os.mkdir(".pstor")
        os.mkdir(".pstor/remotes")
        os.mkdir(".pstor/encrypted")
        os.mkdir(".pstor/data")

        cwd = os.getcwd()
        sh.encfs(os.path.join(cwd,'.pstor/encrypted'),
                 os.path.join(cwd,'.pstor/data'),
                 paranoia=True, extpass="echo '%s'" % args['pass'])

        sh.cp(sh.glob(os.path.join(cwd,'.pstor/data/*')), cwd, symbolic_link=True, recursive=True)

        print "Now you can add remote for this pstore with\n $ pstor remote add"
