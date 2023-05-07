#!/usr/bin/python3
"""Distribute an archive file  to the web servers"""

import os
from fabric.api import *


env.hosts = ['54.87.207.177', '18.209.180.49']
env.user = "ubuntu"
env.password = os.environ['password']


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        splited = archive_path.split(".")[0].split("/")[-1]
        run("sudo mkdir -p /data/web_static/releases/{}".format(splited))
        run("sudo tar -xzvf /tmp/{}.tgz -C\
                /data/web_static/releases/{}/".format(splited, splited))
        run("sudo rm /tmp/{}.tgz".format(splited))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}".format(splited, splited))
        run("sudo rm -rf /data/web_static/releases/\
                {}/web_static/".format(splited))
        run(f"sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}\
                /data/web_static/current".format(splited))
    except Exception:
        return False
    return True
