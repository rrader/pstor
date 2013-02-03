import os
import sh

def mounted():
    try:
        cwd = os.path.join(os.getcwd(), 'files')
        return any(cwd == path.strip() for path in 
                list(sh.awk(sh.grep(sh.mount(), 'encfs'), "{print $3}")))
    except sh.ErrorReturnCode:
        return False