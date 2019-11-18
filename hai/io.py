'''
IO methods
'''
import os


def path_in_dir(directory, filename):
    "return path of file in directory"
    return directory + "/" + filename


def make_parent_dir(filename):
    "Create parent directories for file <filename>."
    path = ""
    for dirname in filename.split("/"):
        dirpath = path + dirname
        if not is_existing_dir(dirpath):
            os.mkdir(dirpath)
        path += dirname + "/"


def is_existing_dir(dirname):
    "Test if a given path is an existing directory."
    return os.path.isdir(dirname)


def remove_empty_dir(dirname):
    "Delete empty directory, if existing."
    if is_existing_dir(dirname):
        os.rmdir(dirname)


def remove_file(filename):
    "Delete empty directory, if existing."
    if is_existing_file(filename):
        os.remove(filename)


def is_existing_file(filename):
    "Test if a given path is an existing file."
    return os.path.isfile(filename)
