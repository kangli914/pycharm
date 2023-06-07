#!/usr/bin/env python3

"""
Ask the user for a directory name. Show all of the files in the directory, as well as how long ago the directory was modified. You will probably want to use combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK) to do this easily.
"""


import os
from pathlib import Path

import arrow
import pprint


# more referece about arrow:
# https://analyticsindiamag.com/complete-guide-to-arrow-a-python-library-for-user-friendly-handling-of-dates-time-and-timestamps/

def open_file_safely(file, mode="r"):
    """Open file saftly otherwise raise exception."""

    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        raise OSError(f"{file} not found!")


def get_stats(item):
    """Show all of the files in the directory, as well as how long ago the directory was modified."""

    # raw is a float
    raw = os.stat(item).st_mtime
    return arrow.get(raw).format('YYYY-MM-DD HH:mm:ss')


if __name__ == "__main__":
    dir = input("Enter a directory name: \n")
    dir_path = Path(dir)
    if dir_path.is_dir():
        pprint.pprint({item.name: get_stats(item) for item in dir_path.rglob("*")})
