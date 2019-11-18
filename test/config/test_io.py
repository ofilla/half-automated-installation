'''
Test IO methods
'''
import os
import pytest
from hai import io


@pytest.mark.io
def test_path_in_dir():
    assert io.path_in_dir("", "") == "/"
    assert io.path_in_dir("<dir>", "") == "<dir>/"
    assert io.path_in_dir("", "<filename>") == "/<filename>"


@pytest.mark.io
def test_dir_exists():
    assert not io.is_existing_dir("not_a_dir")
    assert io.is_existing_dir("hai")


@pytest.mark.io
def test_make_dir():
    dirname = "test_config"
    assert not io.is_existing_dir(dirname)

    io.make_parent_dir(dirname)
    assert io.is_existing_dir(dirname) is True

    os.rmdir(dirname)


@pytest.mark.io
def test_remove_dir():
    dirname = "test_config"
    assert not io.is_existing_dir(dirname)
    os.mkdir(dirname)

    io.remove_empty_dir(dirname)

    assert io.is_existing_dir(dirname) is False


@pytest.mark.io
def test_make_subdir():
    dirname = "test_config"
    subdir = dirname + "/" + "test_config"

    assert io.is_existing_dir(dirname) is False
    assert io.is_existing_dir(subdir) is False

    io.make_parent_dir(subdir)

    assert io.is_existing_dir(dirname) is True
    assert io.is_existing_dir(subdir) is True

    io.remove_empty_dir(subdir)
    io.remove_empty_dir(dirname)


@pytest.mark.io
def test_remove_file():
    """
    * create test file, but fail if file exists
        (do NOT overwrite anything!)
    * delete it tested
    """
    filename = "test_file.towrite"
    open(filename, "x").write('content')
    assert io.is_existing_file(filename)

    io.remove_file(filename)
    assert io.is_existing_file(filename) is False
