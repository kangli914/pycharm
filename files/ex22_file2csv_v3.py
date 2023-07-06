#!/usr/bin/env python3

"""
Create a function, passwd_to_csv, that takes two filenames as arguments:
the first is a passwd-style file to read from, and the second is the name
of a file in which to write the output
"""

import csv
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely
    Accept a filename as an argument and exits if having the issue."""

    # alway better include newline='' when reading csv
    # If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correc
    # https://docs.python.org/3/library/csv.html
    try:
        return open(file, mode, newline='')
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
        # The 'quotechar' parameter specifies the character used for quoting fields. It is set to " by default and it combined used with 'quoating'

        # 'Dialect.quoting' and 'Dialect.quotechar' are mostly good for write out csv data.
        #  For example, the following will quote all the write out data with single quote instead of double quote when writing to the file and the default for Dialect.quoting is defaults to QUOTE_MINIMAL.
        # more rules here https://realpython.com/python-csv/
        writer = csv.writer(fwriter, delimiter="\t", quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
        users = (get_user(row) for row in reader if not row[0].startswith(("#", "\n")))
        writer.writerows(users)


if __name__ == "__main__":
    input = Path("/etc/passwd")
    output = Path.cwd() / "etcout.txt"
    passwd_to_csv(input, output)
