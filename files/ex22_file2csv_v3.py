#!/usr/bin/env python3

"""
Create a function, passwd_to_csv, that takes two filenames as arguments:
the first is a passwd-style file to read from, and the second is the name
of a file in which to write the output
"""

import csv
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        raise OSError("{file} was not found!")


def get_user(row):
    """Return user name and id from the given line."""
    user = row[0]
    id = row[2]
    return user, id


def passwd_to_csv(input_file, output_file):
    """Return username (index 0) and the user ID (index 2) from input."""
    with open_file_safely(input_file, mode="r") as freader, open_file_safely(output_file, mode="w") as fwriter:
        reader = csv.reader(freader, delimiter=":")
        writer = csv.writer(fwriter, delimiter="\t")
        users = (get_user(row) for row in reader if not row[0].startswith(("#", "\n")))
        writer.writerows(users)


if __name__ == "__main__":
    input = Path("/etc/passwd")
    output = Path.cwd() / "etcout.txt"
    passwd_to_csv(input, output)
