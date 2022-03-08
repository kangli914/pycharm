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
    # print(__file__ + "\n")

    with open_file_safe(os.path.join(cwd, "files", "ex18_input.txt")) as f:
        total = sum(int(words) for line in f
                               for words in line.split() if words.isnumeric())

    print(total)
