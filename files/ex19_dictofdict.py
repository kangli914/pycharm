#!/usr/bin/env python3

"""From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell."""


import os
from pathlib import Path
# from collections import defaultdict


def open_file_safely(file, mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error("Erorr in open {file}")


def shell_dict(file):
    """Read from a file and return a dict to dict"""

    '''
    collections = defaultdict(dict)
    The argument passed to defaultdict() specifies the default value that will be returned. In this case, dict() is passed as the default value, which means that a new dictionary will be created as the default value for any non-existing key
    >>> default_dict['key1']
    {}
    >>> d['key1']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'key1'
    '''
    # collections = defaultdict(dict)
    collections = dict()
    with open_file_safely(file) as f:
        for line in f:
            if not line.startswith(("#", "\n")):
                username, second, userid, *rest, homedir = line.strip().split(":")
                collections[username] = {username, userid, homedir}
    return collections


if __name__ == "__main__":
    dir = Path("/etc/")
    file_path = dir / "passwd"
    for k, v in shell_dict(file_path).items():
        print(k, v)
