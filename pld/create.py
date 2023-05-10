#!/usr/bin/python3
from fabric.api import *
import os

env.hosts = ['18.209.180.49', '54.87.207.177']
env.user = "ubuntu"
env.password = os.environ['password']

@task
def deploy():
    if sudo('mkdir -p /pld/').failed:
        print("Creation failed")
    else:
        print("successfully created")
    '''if put('new_pld', '/tmp/').failed:
        print('upload failed')
    else:
        print('successfully uploaded')
    if get('/tmp/', 'download').failed:
        print('download failed')
    else:
        print('download successful')'''
    if local('mkdir -p sideeq').failed:
        print('sideeq creation failed')
    else:
        print('sideeq sef dey sha')
    if  cd('/tmp/'):
        run('ls -l')
