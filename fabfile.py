#!/usr/bin/env python3

from fabric import Connection, task
@task
def deploy(c):
    print(f"Testin")
