import urlparse

from . import Provider

class WebDavProvider(object):
    __metaclass__ = Provider

    @classmethod
    def is_my(cls, url):
        if urlparse.urlparse(url).scheme in ['http', 'https']:
            return cls