#!/usr/bin/env python3

"""A simple words count to mimics to the wc to count the charator, words and line in the give file."""

import os
import sys


def open_file_safely(file):
    try:
        return open(file)
    except OSError:
        sys.exit(f"erorr in open the file {file}")


if __name__ == "__main__":
    cwd_path = os.getcwd()
    print(__file__ + "\n")

    lines = 0
    words = 0
    chars = 0

    with open_file_safely(os.path.join(cwd_path, "files", "ex20_wordcounts_input.txt")) as f:
        for ln in f:
            lines += 1
            # split without any arguments, which causes it to use all whitespace—spaces, tabs, and newlines
            # as delimiters.  e.g. the default separator is any whitespace.
            for wd in ln.strip().split():
                words += 1
                for ch in wd:
                    chars += 1

    print(f"lines {lines}, words {words}, char {chars}")
