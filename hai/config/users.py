'''
Set up user accounts.
'''

from configparser import ConfigParser

USERCONFIG = ConfigParser()


def add_user_config(user, **kwargs):
    """ (str, [key=value]*) -> Section
    Create configuration for user.

    The username is the first argument.
    Further arguments can be added with keyword arguments.
    Possible keyword arguments can be all arguments to the
    *adduser* or *usermod* functions.
    """
    if user in USERCONFIG.sections():
        raise ValueError("username {} is already set".format(user))
    USERCONFIG.add_section(user)

    section = USERCONFIG[user]
    section['user'] = user

    for key, value in kwargs.items():
        section[key] = value

    return section


def example_user_config():
    """ () -> Section
    Create configuration for example user.
    """
    return add_user_config(
        user='user',
        uid=1000,
        gid=1000,
        home='/home/user',
        shell='/bin/bash',
        groups="audio video plugdev netdev lpadmin sudo",
        password='',
        encrypt_home=False,
        no_create_home=False,
        disabled_password=False,
        disabled_login=False,
    )
