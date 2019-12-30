import os
import pytest
from hai import io

TEST_FILENAME = "test_file.towrite"


def setup_function():
    with open(TEST_FILENAME, "x") as file:
        file.write("[example]\n")
        file.write("property = value\n")


def teardown_function():
    if io.is_existing_file(TEST_FILENAME):
        io.remove_file(TEST_FILENAME)


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
    assert io.is_existing_file(TEST_FILENAME) is True
    io.remove_file(TEST_FILENAME)
    assert io.is_existing_file(TEST_FILENAME) is False


@pytest.mark.io
def test_read_simple_config():
    config = io.read_config(TEST_FILENAME)
    example_config = config['example']
    assert example_config['property'] == 'value'


@pytest.mark.io
def test_write_config_overwrite_fails():
    """
    io.write_config shall not overwrite files
    """
    expected = io.read_config(TEST_FILENAME)
    with pytest.raises(FileExistsError):
        io.write_config(expected, TEST_FILENAME)


@pytest.mark.io
def test_write_config():
    """
    Test writing of config,
    assuming reading config works as expected.
    """
    expected = io.read_config(TEST_FILENAME)
    io.remove_file(TEST_FILENAME)

    io.write_config(expected, TEST_FILENAME)

    result = io.read_config(TEST_FILENAME)
    assert result == expected
