'''
Set up user accounts.
'''
from hai.io import make_parent_dir, path_in_dir
CONF_DIR = "config/users"


def create_example():
    "Create example user config"
    filename = get_file_path("example.cfg")
    create_config_file(filename, content="asdf")


def get_file_path(filename):
    "Get path for user config files"
    filename = path_in_dir(CONF_DIR, filename)
    return filename


def create_config_file(filename, content):
    "create user config file"
    make_parent_dir(CONF_DIR)
    open(filename, "x").write(content)
