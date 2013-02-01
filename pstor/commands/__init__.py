from status import status
from init import init
from remote import remote

def call_command(name, args={}):
	globals()[name](**args)