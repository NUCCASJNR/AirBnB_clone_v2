#!/usr/bin/python3
"""Deploys a full archive to the server"""

import os
from fabric.api import env, put, run
from time import strftime

env.hosts = ['18.209.180.49', '54.87.207.177']
env.user = 'ubuntu'
env.password = os.environ['password']


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
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        '''print(file_n)
        print(no_ext)'''
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False


def deploy():
    """Deploys a full archive to the server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
