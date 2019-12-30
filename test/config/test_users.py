import pytest
from hai.config import users

users.CONF_DIR = "test_user_config"


def setup_function():
    users.USERCONFIG = users.ConfigParser()


def test_simple_user_config():
    config = users.add_user_config('username')
    assert len(config.items()) == 1
    assert config['user'] == 'username'


def test_duplicate_user_fails():
    users.add_user_config('username')
    with pytest.raises(ValueError):
        users.add_user_config('username')


def test_user_config_with_keyword_args():
    config = users.add_user_config('user', home="homepath")
    assert len(config.items()) == 2
    assert config['user'] == 'user'
    assert config['home'] == 'homepath'
