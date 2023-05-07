#!/usr/bin/python3
"""deploy to my both servers
"""
import os
from time import strftime
from fabric.api import *


env.hosts = ['ubuntu@54.87.207.177', 'ubuntu@18.209.180.49']
env.password = os.environ['password']


def do_deploy(archive_path):
    """
        Args:
            archive_path: path to the archive file
    """
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        splited = archive_path.split(".")[0].split('/')[-1]
        run('sudo mkdir -p /data/web_static/releases/{}'.format(splited))
        run(f'sudo tar -xzvf /tmp/{splited}.tgz -C\
                /data/web_static/releases/{splited}/')
        run(f"sudo rm /tmp/{splited}.tgz")
        run(f"sudo cp -r /data/web_static/releases/{splited}/web_static/*\
                /data/web_static/releases/{splited}")
        run(f"sudo rm -rf /data/web_static/releases/{splited}/web_static/")
        run(f"sudo rm -rf /data/web_static/releases/{splited}/web_static/")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{splited}\
                /data/web_static/current")
        print(f"New version deployed!")
        return True
    else:
        return False
