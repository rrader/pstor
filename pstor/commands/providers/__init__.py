from ...helpers import import_all

providers = []

class Provider(type):
    def __init__(cls, name, bases, dct):
        providers.append(cls)
        return super(Provider, cls).__init__(name, bases, dct)

import_all(__file__, locals(), globals())

def get_provider_for_url(url):
    for provider in providers:
        if provider.is_my(url):
            return provider
    return None

def get_provider_by_name(name):
    for provider in providers:
        if provider.name() == name:
            return provider
    return None