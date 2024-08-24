""" important imports """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")
    # the format web_static_<year><month><day><hour><minute><second>.tgz
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    # Run the tar command to create the archive
    result = local(f"tar -cvzf {archive_name} web_static", capture=True)
    # Check if the command was successful
    if result.succeeded:
        return archive_name
    else:
        return None
