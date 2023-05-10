#!/usr/bin/python3

import os
from fabric.api import *
from time import strftime
env.user = "ubuntu"
env.hosts = ['54.87.207.177', '18.209.180.49']
env.password = os.environ['password']

def do_pack():
    form = strftime("%Y%m%d%H%M%S")
    '''local('touch new_file_{}'.format(form))'''
    try:
        local('mkdir -p new_versions')
        local('tar -cvzf new_versions/web_static_{}.tgz web_static/'.format(form))
        return 'new_versions/web_static_{}.tgz web_static/'.format(form)
    except Exception:
        return None
