#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to my web servers, using the function do_deploy:
"""

import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ['18.209.180.49', '54.87.207.177']
env.password = os.environ['password']


def do_deploy(archive_path):
    """
    Deploys an archive file to the server
    Args:
        archive_path: path to the archive file on the local machine
                        to be deployed to the server
    Return:
        True: on success
        False: if otherwise
    """

    if not os.path.exists(archive_path):
        return False
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
    run('ln -s {}{} /data/web_static/current'.format(directory, remove_tgz))
