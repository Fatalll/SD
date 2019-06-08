"""This module contains a method for cd command"""

import os


def cd(*args):
    """Change current directory"""

    if len(args) > 1 and len(args[1]) != 1:
        print("cd takes 1 or 0 arguments")
    else:
        try:
            os.chdir(args[1][0] if len(args) else os.getcwd())
            return os.getcwd()
        except Exception as e:
            return str(e)
