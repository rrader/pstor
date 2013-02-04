import os
import sh

def mounted(dir=None):
    try:
        cwd = dir if dir else os.path.join(os.getcwd(), 'files')
        cwd = os.path.realpath(cwd)
        return any(cwd == path.strip() for path in 
                list(sh.awk(sh.cat("/proc/mounts"), "{print $2}")))
    except sh.ErrorReturnCode:
        return False

def umount(remote_dir):
    if not mounted(remote_dir):
        print "<Not mounted>"
        return

    try:
        sh.fusermount('-u', remote_dir)
    except sh.ErrorReturnCode, e:
        print "Error. Can't unmount %s: %s" % (remote_dir, e.message)