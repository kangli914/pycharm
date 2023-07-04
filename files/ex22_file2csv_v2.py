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


def passwd_to_csv(input_file, output_file):
    """Return username (index 0) and the user ID (index 2) from input."""
    with open_file_safely(input_file, mode="r") as freader, open_file_safely(output_file, mode="w") as fwriter:
        reader = csv.reader(freader, delimiter=":")
        writer = csv.writer(fwriter, delimiter="\t")
        # print({get_user(line)[0]: get_user(line)[1] for line in reader if not line[0].startswith("#", "\n")})

        # row is a list not string -- supprise!
        for row in reader:
            # print(row, type(row))
            if not row[0].startswith(("#", "\n")):
                writer.writerow((row[0], row[2]))


if __name__ == "__main__":
    input = Path("/etc/passwd")
    output = Path.cwd() / "etcout.txt"
    passwd_to_csv(input, output)
