import urlparse

from . import Provider

class WebDAV(object):
    __metaclass__ = Provider

    @classmethod
    def is_my(cls, url):
        if urlparse.urlparse(url).scheme in ['http', 'https']:
            return cls

    @classmethod
    def name(cls):
        return cls.__name__