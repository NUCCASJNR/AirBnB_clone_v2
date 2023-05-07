#!/usr/bin/python3
"""Distribute an archve to the web servers"""

from fabric.api import local, put, run, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.160.126.209', '54.208.232.134']


def do_deploy(archive_path):
    """distribute an archive tho the webservers"""
    if not os.path.exists(archive_path):
        return False
    name = archive_path.split("/")[-1].split(".")[0]
    file = archive_path.split("/")[-1]
    if put(archive_path, '/tmp/').failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}'.format(name)).failed:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file, name)).failed:
        return False
    if run('rm /tmp/{}'.format(file)).failed:
        return False
    if run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}'.format(name, name)).failed:
        return False
    if run('rm -rf /data/web_static/releases/{}/web_static'
            .format(name)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name)).failed:
        return False
    return True
