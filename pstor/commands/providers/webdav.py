import urlparse
import os
import sh
import ConfigParser
from time import sleep

from . import Provider

class WebDAV(object):
    __metaclass__ = Provider

    def __init__(self, name):
        self.remote_name = name
        config = ConfigParser.ConfigParser({'username':None, 'pass':None})
        config.read('.pstor/remotes/'+name)
        args = config.get('remote','options').split('\n')
        self.url = config.get('remote','url')
        self.username = args[2]
        self.password = args[3]
        self.remote_dir = '.pstor/webdav_' + self.remote_name

    @classmethod
    def is_my(cls, url):
        if urlparse.urlparse(url).scheme in ['http', 'https']:
            return cls

    @classmethod
    def name(cls):
        return cls.__name__

    def up(self):
        remote_dir = self.remote_dir
        if not os.path.exists(remote_dir):
            os.mkdir(remote_dir)

        sh.wdfs(self.url, remote_dir,
            o="username={},password={}".format(self.username, self.password))
        sleep(1)

        remote_dir = os.path.join(self.remote_dir, 'pstor')
        sh.rsync(remote_dir, '.pstor/encrypted/', recursive=True, delete=True)

    def down(self):
        try:
            sh.fusermount('-u', self.remote_dir)
        except sh.ErrorReturnCode:
            pass

    def sync(self):
        remote_dir = os.path.join(self.remote_dir, 'pstor')
        if not os.path.exists(remote_dir):
            os.mkdir(remote_dir)

        sh.rsync('.pstor/encrypted/', remote_dir, recursive=True, delete=True)