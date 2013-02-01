import os
from ..helpers import exceptions

def status(**args):
    if os.path.isdir(".pstor"):
        pass
    else:
        raise exceptions.PstorException("Not initialized in this directory. Do\n $ pstor init")