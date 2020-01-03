'''
Set up user accounts.
'''

import subprocess
from hai import io

DRYRUN = True
USERADD_PARAMETERS = {
    "base-dir",
    "comment",
    "home-dir",
    "defaults",
    "expiredate",
    "inactive",
    "gid",
    "groups",
    "help",
    "skel",
    "key",
    "no-log-init",
    "create-home",
    "no-create-home",
    "no-user-group",
    "non-unique",
    "password",
    "system",
    "root",
    "shell",
    "uid",
    "user-group",
    "selinux-user",
    "extrausers"
}
USERMOD_PARAMETERS = {
    "comment",
    "home",
    "expiredate",
    "inactive",
    "gid",
    "groups",
    "lock",
    "non-unique",
    "password",
    "root",
    "shell",
    "uid",
    "unlock",
    "add-sub-uids",
    "del-sub-uids",
    "add-sub-gids",
    "del-sub-gids"
}


def configure_all(conffile='users.cfg'):
    """ (str) -> int
    Confiture user accounts.
    Give the path to the users config file as argument.
    """
    print("user configuration: " + conffile)

    config = io.read_config(conffile)
    for section in config.sections():
        configure_user(config[section])


def configure_user(config):
    """ (Section) -> None
    Configure single useraccount.
    Following keys are available:
        disabled_login: (bool)
        disabled_password: (bool)
        encrypt_home: (bool)
        gid: primary group id, (int)
        user: username (str)
        uid: user id (int)
        home: path to home directory (str)
        no_create_home: (bool)
        groups: list of groups, separated by comma (str)
    #    password: encrypted password (str)
        shell: path to shell (str)
    """
    username = config['user']
    print("configuring user " + username)

    user_found = is_existing_user(username)
    if not user_found:
        print("  add new user")
        call_command_with_parameter(config, 'useradd', USERADD_PARAMETERS)
        print("  modify new user")
    else:
        print("  modify existing user")
    call_command_with_parameter(config, 'usermod', USERMOD_PARAMETERS)


def call_command_with_parameter(config, command, command_parameters):
    """ (Section, str, set) -> None
    Run a command with the system shell.
    Use parameters from config, that belong to this command.
    """

    command = create_command_list(config, command, command_parameters)
    if DRYRUN:
        return

    return_value = subprocess.call(command)
    if return_value != 0:
        raise RuntimeWarning("command failed: {}".format(" ".join(command)))


def create_command_list(config, command, parameter_set):
    """ (Section, str, set) -> list
    Create a list of the command, with all parameters
    from config configured. These parameters are filtered
    with the parameter_set belonging to command.
    """
    params = get_function_params(config, parameter_set)

    command_list = [command]
    for param in params:
        value = config.get(param)
        if value.lower() == 'false':
            continue

        if value.lower() == 'true':
            command_list.append('--' + param)
        else:
            command_list.append("--" + param)
            command_list.append(value)

    command_list.append(config['user'])
    print('\t' + " ".join(command_list))
    return command_list


def is_existing_user(username):
    """ (str) -> bool
    Checks if user `username` exists.
    Does so with checking the return value of
    the `id` command from linux.
    """
    check_needed_command('id')

    return_value = subprocess.call(
        ["id", username],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    user_found = return_value == 0
    return user_found


def check_needed_command(command):
    """ (str) -> None
    Check if *command* is an callable
    in the system shell. Raise, if not.
    """
    return_value = subprocess.call(command, stdout=subprocess.DEVNULL)
    if return_value != 0:
        raise RuntimeError("command 'id' cannot be executed!")


def get_function_params(config, params_set):
    """ (Section, set) -> set
    Find parameters in *config* that are also in *params_set*.
    """
    given_params = set(config.keys())
    matched_params = given_params.intersection(params_set)
    return matched_params
