"""This module contains a method for ls command"""

import os


def ls(*args):
    """Print specified directory"""

    if len(args) > 1 and len(args[1]) != 1:
        print("ls takes 1 or 0 arguments")
    else:
        try:
            return '\n'.join(os.listdir(args[1][0] if len(args) else os.getcwd()))
        except Exception as e:
            return str(e)
