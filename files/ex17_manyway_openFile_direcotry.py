#!/usr/bin/env python3

"""Note down the different ways to open files in directory.
The 3 most common ways: (p 87)
 - os.listdir
 - glob.glob
 - pathlib.Path
Serve as a standard template.

os.listdir:
 - The downside of os.listdir is it returns a list of filenames WITHOUT the direcotry name so you will need os.path.join to give the full path
 - also os.listdir does not allow you to filter the filnames by a pattern

glob.glob:
- it returns a list of strings with each string containing the complete path to the file.

pathlib.Path:
 - provides us with an object-oriented API to the filesystem

open file:
 # https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python
"""

import os
import pathlib
import sys
from glob import glob


def open_file_safe(file):
    """Open the file safely.

    Accept a filename as an argument, and exit if having the error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encountered when opening the file {file}!")


def open_directory_1(dir):
    # os.listdir Only returns a list of filenames without the directory name,
    return [open_file_safe(os.path.join(dir, file_name)) for file_name in os.listdir(dir) if file_name.endswith(".txt") and os.path.isfile(os.path.join(dir, file_name))]


def open_directory_2(dir):
    # glob.glob to returns a list of filenames
    return [open_file_safe(file) for file in glob(f"{dir}/*.txt", recursive=True)]
    # open all the files and sub-directory
    # for one_filename in glob.glob(f"{dir}/*", recursive=True):


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
    '''
    # If you want to get a list of files matching a pattern,using p.glob():
    for one_filename in p.glob('*.conf'):
        print(one_filename)
    '''

    print(" --- path.iterdir(): ---")
    for child in p.iterdir():
        # <class 'pathlib.PosixPath'> object than a string
        print(child)

    # path.glob(patten) Glob the given relative pattern in the directory represented by this path, 
    # yielding all matching *files* (return)
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path
    # with the addition of “**” which means “this directory and all subdirectories, recursively”
    return [open_file_safe(one_file) for one_file in p.glob("**/*.txt")]


if __name__ == "__main__":
    print(" --- pathlib.Path() ---")
    for one in open_directory_3("files"):
        print(one)

    print(" --- lob.glob() ---")
    for one in open_directory_2("files"):
        print(one)

    print(" --- os.listdir() ---")
    for one in open_directory_1("files"):
        print(one)
