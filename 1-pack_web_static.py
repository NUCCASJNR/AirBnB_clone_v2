#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.

Prototype: def do_pack():
All files in the folder web_static must be added to
the final archive
All archives must be stored in the folder versions
(your function should create this folder if it doesn’t exist)
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path
if the archive has been correctly generated.
Otherwise, it should return None
"""

import os
from time import strftime
from fabric.api import local


def do_pack():
    """
    pack prototype
    """

    archive_folder = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(archive_folder))
        return "versions/web_static_{}.tgz".format(archive_folder)
    except Exception as a:
        return None
