#!/usr/bin/env python3

"""Find all of the words that contain only integers and sum them by iterating over lines of a text file"""

import os
import sys


def open_file_safe(file):
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encounter in opening the file {file}")


if __name__ == "__main__":
    cwd = os.getcwd()

    for line in open_file_safe(os.path.join(cmd, "ex18_input.txt"))

    