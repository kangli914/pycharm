#!/usr/bin/env python3

"""A prompt for user to count words apperaiance.

User is asked to give file and many words separated by spaces in one line.
"""

import os
import sys
from collections import defaultdict


def open_file_saftly(file):
    """Open the file saftly.

    Accept a filename as an arugment. It throws the rrors and exits if having error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encountered in open the file {file}")


def words_count(file, words_tuple):
    """Coun the words."""
    collections = defaultdict(int)
    # or
    # collections = dict.fromkeys(words, 0)

    with open_file_saftly(os.path.join(curr_dir, "files", file)) as f:
        for line in f:
            for a_words in line.strip().split():
                if a_words in words_tuple:
                    collections[a_words] += 1

    return collections


if __name__ == "__main__":

    given = input("Please entry file and words in the following format:\n  filename words1 words2...\n").strip()
    file, *words_tuple = given.strip().split()
    curr_dir = os.getcwd()
    # print(__file__ + "\n")

    print(words_count(file, words_tuple))
