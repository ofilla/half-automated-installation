"""
hai.__main__ -- Half-Automated Installation

hai.__main__ is a description

Half-Automated Installation

@author:     Oliver Filla

@copyright:  2019. All rights reserved.

@license:    license

@contact:    ocl@hotmail.de
@deffield    updated: Updated
"""

import sys
import os

from hai.config import users

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2019-11-17'


def main(argv=None):
    """Command line options."""

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version_message = '%%(prog)s v%s (%s)' % (__version__, __date__)
    program_shortdesc = __doc__.split("\n")[1]
    program_license = """%s

  Created by user_name on %s.
  Copyright 2019 organization_name. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
""" % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(
            description=program_license,
            formatter_class=RawDescriptionHelpFormatter
        )

        parser.add_argument(
            "-c",
            "--configuration-directory",
            dest="confpath",
            action="store",
            required=True,
            help="path to configuration files"
        )
        parser.add_argument(
            "-d",
            "--dry-run",
            dest="dryrun",
            action="store_true",
            default=False,
            help="Do not modify the system"
        )
        parser.add_argument(
            "-u",
            "--users",
            dest="users",
            action="store_true",
            default=False,
            help="set up / modify user accounts"
        )
        parser.add_argument(
            '-V',
            '--version',
            action='version',
            version=program_version_message
        )

        # Process arguments
        args = parser.parse_args()
        dryrun = args.dryrun
        confpath = args.confpath
        if confpath[-1] != '/':
            confpath += '/'

        print("Path to configuration files:" + confpath[:-1])
        users.DRYRUN = dryrun
        if args.users:
            users.configure_all(confpath + 'users.cfg')

        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
