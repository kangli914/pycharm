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

    # use iterdir()
    if dir_path.is_dir():
        print({item.name: get_md5(dir_path / item) for item in dir_path.iterdir() if item.is_file()})

    #  use rglob("*") to recursive the iterate
    if dir_path.is_dir():
        print({item.name: get_md5(dir_path / item) for item in dir_path.rglob("*") if item.is_file()})


    """
    from pathlib import Path

    def iterate_files_recursively(directory):
        # Create a Path object for the specified directory
        path = Path(directory)

        # Use rglob to recursively iterate over json files
        for file_path in path.rglob("*.json"):
            if file_path.is_file():
                # Process the file as needed
                print(file_path)

    # Example usage
    directory_path = "/path/to/directory"
    iterate_files_recursively(directory_path)
    """
