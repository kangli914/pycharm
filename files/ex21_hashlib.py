#!/usr/bin/env python3


"""
Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a user-
specified directory. Then print all of the filenames and their MD5 hashes.
"""


import hashlib
from pathlib import Path


def open_file_safely(file, mode="rb"):
    """Open file safely."""

    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        raise OSError("f{file} not found!")


def get_md5(file):
    with open_file_safely(file) as f:
        return hashlib.md5(f.read()).hexdigest()


if __name__ == "__main__":
    dir_path = Path.cwd() / "files/tmp"

    if dir_path.is_dir():
        print({item.name: get_md5(dir_path / item) for item in dir_path.iterdir() if item.is_file()})
