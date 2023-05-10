#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:
"""
from fabric.api import *
import os

env.hosts = ['18.209.180.49', '54.87.207.177']
env.user = 'ubuntu'
env.password = os.environ['password']

def do_clean(number=0):
    """
    Deletes archive files
    """
    if number == 0 or number == 1:

