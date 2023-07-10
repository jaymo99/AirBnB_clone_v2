#!/usr/bin/python3
'''Module uses Fabric for web_static deployment
'''

import os

from datetime import datetime
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['100.26.213.68', '35.175.63.17']


def do_deploy(archive_path):
    '''Distributes an archive to web servers
    '''
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ of web server
        put(archive_path, '/tmp/')

        # Uncompress the archive
        file_name = os.path.basename(archive_path)
        dir_name, extension = os.path.splitext(file_name)
        run("mkdir -p /data/web_static/releases/{}".format(dir_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(file_name, dir_name))

        # Delete the archive from the web server
        release = "/data/web_static/releases/{}".format(dir_name)
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(release, release))
        run("rm -rf {}/web_static".format(release))

        # Recreate symlink linked to the new version of the code
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(dir_name))
    except Exception:
        return False

    print("New version deployed!")
    return True
