#!/usr/bin/env python3

"""Open an HTTP servers log file and summarize how many requests resulted in numeric
response codes—202, 304, and so on.

# many way to read a file # https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python
"""

import os
import sys
from collections import defaultdict


def open_file_safely(file):
    """Open the file safely.

    Accept a filename as an argument and exits if having the issue.
    """
    try:
        return open(file, "r")
    except OSError:
        sys.exit(f"error encountered when opening the file {file}")


if __name__ == "__main__":
    # print(__file__)
    # print(os.path.dirname(__file__))

    response_codes = defaultdict(int)
    with open_file_safely(os.path.join(os.getcwd(), "mini-access-log.txt")) as f:
        for one_line in f:
            response_codes[one_line.split()[8]] += 1

    for k, v in response_codes.items():
        print(k, v)
