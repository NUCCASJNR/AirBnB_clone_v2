#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder /data/web_static/releases/<archive
filename without extension> on the web server
Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on the
web server, linked to the new version of your code (/data/web_static
/releases
/<archive filename without extension>)
All remote commands must be executed on your both web
servers (using env.hosts = ['<IP web-01>', 'IP web-02']
variable in your script)
Returns True if all operations have been done correctly, otherwise
returns False
You must use this script to deploy it on your servers: xx-web-01
and xx-web-02
In the following example, the SSH key and the username
used for accessing to the server are passed in the command
line. Of course, you could define them as Fabric environment
variables (ex: env.user =...)

Disclaimer: commands execute by Fabric displayed below
are linked to the way we implemented the archive function
do_pack - like the
mv command - depending of your implementation of it,
you may don’t need it
"""

import os
from time import strftime
from fabric.api import *
# from fabric import Connection, task
import sys


'''env.hosts = os.environ['hosts'].split(',')
env.passwords = {}
for i, host in enumerate(env.hosts):
    env.passwords[host] = os.environ['passwords'].split(',')[i]'''

env.hosts = ['ubuntu@54.87.207.177', 'ubuntu@18.209.180.49']
env.password = os.environ['password']


def do_deploy(archive_path):
    """
        Args:
            archive_path: path to the archive file
    """

    '''env.host_string = os.environ['hostname']
    env.password = os.environ['password']'''
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        splited = archive_path.split(".")[0].split('/')[-1]
        run('sudo mkdir -p /data/web_static/releases/{}'.format(splited))
        run(f'sudo tar -xzvf /tmp/{splited}.tgz -C\
                /data/web_static/releases/{splited}/')
        run(f"sudo rm /tmp/{splited}.tgz")
        run(f"sudo cp -R -r /data/web_static/releases/{splited}/web_static/*\
                /data/web_static/releases/{splited}")
        run(f"sudo rm -rf /data/web_static/releases/{splited}/web_static/")
        run(f"sudo rm -rf /data/web_static/releases/{splited}/web_static/")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{splited}\
                /data/web_static/current")
        print(f"New version deployed!")
    else:
        return False
