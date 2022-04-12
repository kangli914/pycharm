#!/usr/bin/env python3

"""Given a directory, read through each file and count the frequency of each letter.

Force letters to be lowercase, and ignore nonletter characters, and find the five most common letters
across all of these files.
"""

import os
import sys
from collections import defaultdict


def open_file_safely(file):
    """Open the file saftly.

    Accept a filename as an arugment. It throws the errors and exits if having error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encoutnered in open the file {file}")


def all_files(path):
    """Return a generator of a list of file TextIO objects in the given directory."""
    files_obj_list = (open_file_safely(os.path.join(path, filename)) for filename in os.listdir(path) if filename.endswith(".txt") and os.path.isfile(os.path.join(path, filename)))

    print(type(files_obj_list))  # <class 'generator'>

    return files_obj_list


if __name__ == "__main__":
    path = os.getcwd()

    for line in all_files(os.path.join(path, "files")):
        print(line)
