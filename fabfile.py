#!/usr/bin/python3
"""Fabric script that generates a
from invoke import task
from datetime import datetime
import os


@task
def do_pack(c):
    """Compress web_static into a .tgz archive."""
    # Create versions directory if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')
    # Generate a timestamp for the archive name
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{time_str}.tgz"
    # Pack the web_static directory
    result = c.run(f"tar -cvzf {archive_path} web_static", hide=True)
    if result.ok:
        print(f"Packed web_static to {archive_path}")
        return archive_path
    else:
        print("Failed to create archive")
        return None
