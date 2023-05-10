#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['18.209.180.49', '54.87.207.177']
env.user = "ubuntu"
env.password = os.environ['password']

def deploy():
    if sudo('mkdir -p /pld/').failed:
        print("Creation failed")
    else:
        print("successfully created")
    if put('/home/alareef/learning_python', '/tmp/').failed:
        print('upload failed')
    else:
        print('successfully uploaded')
