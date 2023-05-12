#!/usr/bin/python3
"""Deploys a full archive to the server"""

import os
from fabric.api import *
from time import strftime

env.user = "ubuntu"
env.hosts = ['18.209.180.49', '58.87.207.177']
env.password = os.getenv('password')


def do_pack():
    """generate a tgz archive"""

    archive_folder = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(archive_folder))
        return "versions/web_static_{}.tgz".format(archive_folder)
    except Exception as a:
        return None


def do_deploy(archive_path):
    """
    Deploys an archive file to the server
    """

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        split_slash = archive_path.split("/")[-1]
        remove_tgz = split_slash.split(".")[0]
        directory = '/data/web_static/releases/'
        run('mkdir -p {}{}'.format(directory, remove_tgz))
        run('tar -xzf /tmp/{0}.tgz -C {1}{0}'.format(remove_tgz, directory))
        run('rm /tmp/{}.tgz'.format(remove_tgz))
        run('mv {0}{1}/web_static/* {0}{1}'.format(directory, remove_tgz))
        run('rm -rf {}{}/web_static'.format(directory, remove_tgz))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}\
                /data/web_static/current'.format(directory, remove_tgz))
        return True
    except Exception as e:
        return False


def deploy():
    """Deploys a full archive to the server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
