'''
tests for user config
'''
from hai.config import user
from hai import io

user.CONF_DIR = "test_user_" + user.CONF_DIR
TEST_FILE_NAME = "example.cfg"


def test_get_file_path():
    assert user.get_file_path("") == user.CONF_DIR + "/"
    expected = user.CONF_DIR + "/" + "<FILENAME>"
    assert user.get_file_path("<FILENAME>") == expected


def test_create_file():
    filename = "test_file"
    user.create_config_file(filename, "nothing")

    assert io.is_existing_file(filename)

    io.remove_file(filename)


def test_create_example():
    """
    create example user config
    """
    user.create_example()
    conf_file = user.get_file_path(TEST_FILE_NAME)
    assert io.is_existing_file(conf_file)

    io.remove_file(conf_file)


def test_valid_user_config():
    "check TEST_FILE_NAME on Validity"
    user.create_example()
    conf_file = user.get_file_path(TEST_FILE_NAME)
    config = user.read_config(conf_file)
