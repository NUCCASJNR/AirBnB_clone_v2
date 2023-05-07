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
    splited = archive_path.split("/")[-1].split(".")[0]
    name = archive_path.split("/")[-1]
    if put(archive_path, '/tmp/').failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}".format(splited))\
            .failed:
        return False
    if run("tar -xzf /tmp/{}.tgz -C /data/web_static/\
            releases/{}/".format(name, splited)).failed:
        return False
    if run("rm /tmp/{}.tgz".format(name)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}".format(splited, splited)).failed:
        return False
    if run("rm -rf /data/web_static/releases/\
            {}/web_static/".format(splited)).failed:
        return False
    if run(f"rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}\
            /data/web_static/current".format(splited)).failed:
        return False
    return True
