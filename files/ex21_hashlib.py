#!/usr/bin/env python3

"""Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a user
specified directory. Then print all of the filenames and their MD5 hashes.

The 3 most common ways to list files in a directory: (p 87)
"""


import hashlib
import pathlib
import sys


def open_file_safe(file):
    """Open the file safely.

    Accept a filename as an argument, and exits if having the issue.
    """
    try:
        # read in as bytes
        return open(file, "rb")
    except OSError:
        sys.exit(f"error encountered when opening the file {file}!")


def open_files_directory(dir):
    """Open the file from a given directory.
    """
    # creating a pathlib.Path object, which represents a file or directory
    p = pathlib.Path(dir)

    # print(p.glob("**/*.txt"))
    # for child in p.iterdir():
    #     print(child)

    return (open_file_safe(one_file) for one_file in p.glob("**/*.txt"))


def hash_file(file):
    """Hash the md5 a file.

    hash_md5.hexdigest() will return the hex string representation for the digest.
    """
    hash_md5 = hashlib.md5()
    with file as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()


if __name__ == "__main__":
    for file in open_files_directory('./files'):
        print(f"{file.name}", hash_file(file))
