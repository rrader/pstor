import urlparse
import os
import sh
import ConfigParser
from time import sleep

from . import Provider
from ...helpers import exceptions, pstor

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

    def mount(self, remote_dir):
        if pstor.mounted(remote_dir):
            return

        sh.wdfs(self.url, remote_dir,
            o="username={},password={}".format(self.username, self.password))

    def up(self):
        remote_dir = self.remote_dir
        if not os.path.exists(remote_dir):
            os.mkdir(remote_dir)

        tries = 3
        while tries > 0:
            self.mount(remote_dir)
            sleep(1)

            try:
                sh.ls(remote_dir)
            except sh.ErrorReturnCode:
                pstor.umount(remote_dir)
            else:
                break

            tries -= 1
        else:
            raise exceptions.PstorException("Can't ls in mounted webdav directory")

        remote_dir = os.path.join(self.remote_dir, 'pstor/')
        #TODO: check if mounted correctly
        if not os.path.exists(remote_dir):
            os.mkdir(remote_dir)
        sh.rsync(remote_dir, '.pstor/encrypted', recursive=True)

    def down(self):
        try:
            pstor.umount(self.remote_dir)
        except sh.ErrorReturnCode:
            pass

    def sync(self):
        if not pstor.mounted(self.remote_dir):
            print "<Not mounted>"
            return

        remote_dir = os.path.join(self.remote_dir, 'pstor')
        if not os.path.exists(remote_dir):
            os.mkdir(remote_dir)
        #TODO: do sync only if mounted
        sh.rsync('.pstor/encrypted/', remote_dir, recursive=True, delete=True)