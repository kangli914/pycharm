#!/usr/bin/env python3

"""Sum tow columns container a number and ignore any line does not contain two numeric columns."""

import os
import sys


def open_file_safe(file):
    try:
        return open(file)
    except OSError:
        sys.exit(f"having problem openning the file {file}!")


if __name__ == "__main__":
    cwd_path = os.getcwd()
    print(__file__ + "\n")

    total = 0
    with open_file_safe(os.path.join(cwd_path, "files", "ex18_2-cols-numbers.txt")) as f:
        for line in f:
            # str.strip removes the whitespace—the space character, as well as \n, \r, \t
            # split without any arguments, which causes it to use all whitespace—spaces, tabs, and newlines
            # as delimiters.  e.g. the default separator is any whitespace.
            first_words, second_words, *extra = line.strip().split("\t")
            if not extra:
                if first_words.isnumeric() and second_words.isnumeric():
                    total += int(first_words) * int(second_words)
    print(total)
