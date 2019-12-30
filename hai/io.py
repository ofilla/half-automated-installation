'''
IO methods
'''
import os
from configparser import ConfigParser

TEST_FILENAME = "test_file.towrite"


def path_in_dir(directory, filename):
    """ (str, str) -> str
    Return path of file in directory
    """
    return directory + "/" + filename


def make_parent_dir(filename):
    """ (str) -> None
    Create parent directories for file <filename>.
    """
    path = ""
    for dirname in filename.split("/"):
        dirpath = path + dirname
        if not is_existing_dir(dirpath):
            os.mkdir(dirpath)
        path += dirname + "/"


def is_existing_dir(dirname):
    """ (str) -> boolean
    Test if a given path is an existing directory.
    """
    return os.path.isdir(dirname)


def remove_empty_dir(dirname):
    """ (str) -> None
    Delete empty directory, if existing.
    """
    if is_existing_dir(dirname):
        os.rmdir(dirname)


def remove_file(filename):
    """ (str) -> None
    Delete empty directory, if existing.
    """
    if is_existing_file(filename):
        os.remove(filename)


def is_existing_file(filename):
    """ (str) -> None
    Test if a given path is an existing file.
    """
    return os.path.isfile(filename)


def read_config(filename):
    """ (str) -> ConfigParser
    Read a config file and return lines as dict.
    """
    config = ConfigParser()
    config.read_string(open(filename).read(), filename)
    return config


def write_config(config, filename):
    """ (ConfigParser, str) -> None
    Write config to given filename
    """
    config.write(open(filename, 'x'))
