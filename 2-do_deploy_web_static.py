#!/usr/bin/python3
"""
distributes an archive to my web servers using
the do_deploy function

"""

import os
from fabric.api import *


env.hosts = ['54.87.207.177', '18.209.180.49']
env.user = "ubuntu"
env.password = os.environ['password']


def do_deploy(archive_path):
    """deploy to the server"""

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        splited = archive_path.split(".")[0].split("/")[-1]
        run('sudo mkdir -p /data/web_static/releases/{}'.format(splited))
        run(f'sudo tar -xzvf /tmp/{splited}.tgz -C\
                /data/web_static/releases/{splited}/')
        run(f"sudo rm /tmp/{splited}.tgz")
        run(f"sudo mv /data/web_static/releases/{splited}/web_static/*\
                /data/web_static/releases/{splited}")
        run(f"sudo rm -rf /data/web_static/releases/{splited}/web_static/")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{splited}\
                /data/web_static/current")
        return True
    except Exception as e:
        return False
