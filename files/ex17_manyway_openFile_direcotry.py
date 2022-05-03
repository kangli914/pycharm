#!/usr/bin/env python3

"""Note down the different ways to open files in directory.

Serve as a standard template.
"""

from fileinput import filename
import os
import pathlib
import sys


def open_file_safe(file):
    """Open the file safely.

    Accept a filename as an argument, and exit if having the error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encountered when opening the file {file}!")


def open_directory_1(dir):
    # os.listdir returns a list of filenames without the directory name,
    return [open_file_safe(os.path.join(dir, file_name)) for file_name in os.listdir(dir)]


def open_directory_3(dir):
    """Open the direcotry using pathlib.

    Good reference about pathlib: 
    - https://realpython.com/python-pathlib/
    - https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
    """
    # pathlib.Path object, which represents a file or directory
    p = pathlib.Path(dir)

    # path.iterdir() when the path points to a directory, yield path objects of the directory contents:
    # following list out the cotents of given directory
    print(" --- path.iterdir(): ---")
    for child in p.iterdir():
        # <class 'pathlib.PosixPath'> object than a string
        print(child)

    # path.glob(patten) Glob the given relative pattern in the directory represented by this path, 
    # yielding all matching *files* (return)
    return [open_file_safe(one_file) for one_file in p.glob("*.txt")]


if __name__ == "__main__":
    print(" --- pathlib.Path() ---")
    for one in open_directory_3("files"):
        print(one)

    print(" --- os.listdir() ---")
    for one in open_directory_1("files"):
        print(one)
