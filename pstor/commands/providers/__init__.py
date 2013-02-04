from ...helpers import import_all

providers = []

class Provider(type):
    def __init__(cls, name, bases, dct):
        providers.append(cls)
        return super(Provider, cls).__init__(name, bases, dct)

import_all(__file__, locals(), globals())

def get_provider(url):
    for provider in providers:
        if provider.is_my(url):
            return provider
    return None