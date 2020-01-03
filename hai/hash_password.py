import crypt
import getpass
import sys

def hash_password():
    pw = getpass.getpass('Enter new UNIX password: ')
    validate = getpass.getpass('Retype new UNIX password: ')
    if pw != validate:
        sys.stderr.write("Sorry, passwords do not match\n")
        sys.exit(1)

    salt = crypt.mksalt()
    return crypt.crypt(pw, salt=salt)


if __name__ == "__main__":
    print(hash_password())
