import os
from ..helpers import exceptions

cmd_list = {}

def cli_command(func):
    cmd_list[func.__name__] = func
    return func

def inside_pstor(func):
    def _inside_pstor(*args, **kwargs):
        if not os.path.isdir(".pstor"):
            raise exceptions.PstorException("No pstor here")
        func(*args, **kwargs)
    _inside_pstor.__name__ = func.__name__
    return _inside_pstor

def call_command(name, args={}):
    cmd_list[name](**args)

import init, status, remote, destroy, up, down

__all__ = cmd_list.keys()