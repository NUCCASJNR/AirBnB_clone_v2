#!/usr/bin/python3
import os
from fabric.api import *
from time import strftime
env.user = "ubuntu"
env.hosts = ['54.87.207.177', '18.209.180.49']
env.password = os.environ['password']

def do_deploy(archive_path):
    if os.path.exists(archive_path):
        try:
            directory = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            remove = archive_path.split("/")[1]
            print(remove)
            dot = remove.split(".")[0]
            print(dot)
            run('mkdir -p {}{}'.format(directory, dot))
            run('tar -xzf /tmp/{} -C {}{}'.format(
        except Exception:
            return False
