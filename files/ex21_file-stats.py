#!/usr/bin/env python3

"""Ask the user for a directory name. Show all of the files in the directory, as well
as how long ago the directory was modified. You will probably want to use a combination 
of os.stat and the Arrow package
"""

import glob
import os
import pathlib
import sys

import arrow


def open_file_safe(file):
    """Open the file safely.

    Accept a file name as an argument and exits if having the issue.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encountered when opening the file {file}")


def open_files_directory(dir):
    """Return the files from a given directory."""

    p = pathlib.Path(dir)
    # print(p.glob("**/*.txt"))
    # for child in p.iterdir():
    #     print(child)

    return (open_file_safe(one_file) for one_file in p.iterdir())


if __name__ == "__main__":
    dir = input("give a directory:")
    # creating a pathlib.Path object, which represents a file or directory
    p = pathlib.Path(dir)

    for child in p.iterdir():
        print(f"file: {child.name}, last modified time: {arrow.get(os.stat(child)[-1]).format('YYYY-MM-DD HH:mm:ss')}")

    output = {}
    for child_file in glob.glob(f"{dir}/*", recursive=True):
        mod_time = os.stat(child_file).st_mtime
        output[child_file] = (arrow.now() - arrow.get(1503636889)).days
    for k, v in output.items():
        print(k, v)
