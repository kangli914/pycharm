#!/usr/bin/env python3

"""Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation."""

import os
import sys
from collections import defaultdict


def open_file_safe(file):
    """Open file safe."""
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encountered in open file {file}")


if __name__ == "__main__":
    collections = defaultdict(int)

    # collections
    vowel = ["a", "e", "i", "o", "u"]

    cwd = os.getcwd()
    with open_file_safe(os.path.join(cwd, "files", "ex18_vowel.txt")) as f:

        for line in f:
            # str.strip removes the whitespace chars (witesapce = spaces, tabs, and newlines.), as well as \n, \r, \t
            for words in line.lower().strip().split():
                for char in words:
                    if char in vowel:
                        collections[char] += 1


for k, v in collections.items():
    print(f"key: {k}, value: {v}")
