import os
from ..helpers import exceptions, import_all

cmd_list = {}
cmd_args_list = []

def cli_command(args=None):
    def _cli_command(func):
        cmd_list[func.__name__] = func
        cmd_args_list.append(args)
        return func
    return _cli_command

def inside_pstor(func):
    def _inside_pstor(*args, **kwargs):
        if not os.path.isdir(".pstor"):
            raise exceptions.PstorException("Not initialized in this directory. Do\n $ pstor init")
        func(*args, **kwargs)
    _inside_pstor.__name__ = func.__name__
    return _inside_pstor

def call_command(name, args={}):
    cmd_list[name](**args)

import_all(__file__, locals(), globals())

__all__ = cmd_list.keys()