cmd_list = {}

def cli_command(func):
    cmd_list[func.__name__] = func
    return func

def call_command(name, args={}):
    cmd_list[name](**args)

import init, status, remote, destroy

__all__ = cmd_list.keys()