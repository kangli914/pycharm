#!/usr/bin/env python3

"""Find all of the words that contain only integers and sum them by iterating over lines of a text file"""

import os
import sys
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error(f"Encountered error when open the file {file}!")


if __name__ == "__main__":

    # Option 1:
    cwd = os.getcwd()
    print(__file__ + "\n")

    # str.strip removes the whitespace—the space character, as well as \n, \r, \t
    with open_file_safely(os.path.join(cwd, "files", "ex18_input.txt")) as f:
        # split without any arguments, which causes it to use all whitespace—spaces, tabs, and newlines as delimiters. e.g. the default separator is any whitespace.
        total = sum(int(words) for line in f
                    for words in line.strip().split() if words.isnumeric())

    # Option 2: using path
    root_path = Path.cwd()
    file = root_path / "files" / "ex18_input.txt"

    if file.exists():
        total = 0
        with open_file_safely(file, mode="r") as f:
            # print(line, end="")
            for line in f:
                for words in line.strip().split():
                    if words.isnumeric():
                        total += int(words)
    print(total)
