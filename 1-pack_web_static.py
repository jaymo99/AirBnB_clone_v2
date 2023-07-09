#!/usr/bin/python3
'''Module uses Fabric for web_static compression
'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''generates a .tgz archive from the contents of
    web_static folder
    '''
    local("mkdir -p versions")
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    zip_path = "versions/web_static_{}.tgz".format(time_stamp)
    status = local("tar -czvf {} web_static".format(zip_path), capture=True)
    if status.failed:
        return None
    return zip_path
