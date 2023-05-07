#!/usr/bin/python3
"""Deploys a full archive to the server"""

import os
from fabric.api import env, put, run
from time import strftime

env.hosts = ['18.209.180.49', '54.87.207.177']
env.user = 'ubuntu'
env.password = os.environ['password']


def do_pack():
    """
    pack prototype
    """

    archive_folder = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(archive_folder))
        return "versions/web_static_{}.tgz".format(archive_folder)
    except Exception as a:
        return None


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
        return True
    except Exception as e:
        return False


def deploy():
    """Deploys a full archive to the server"""
    file = do_pack()
    if file is None:
        return none
    return do_deploy(file)
