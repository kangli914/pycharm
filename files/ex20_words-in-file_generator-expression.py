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
    """Count the words.

    Reference: Https://www.teclado.com/30-days-of-python/python-30-day-23-generators-yield
    """
    collections = defaultdict(int)

    with open_file_saftly(os.path.join(curr_dir, "files", file)) as f:

        # use Generator Expressions here!!
        words = (a_words for line in f for a_words in line.strip().split() if a_words in words_tuple)

        # Have to put `for..in`` within the file open code block to avoid "ValueError: I/O operation on closed file." error
        # regarding "ValueError: I/O operation on closed file." error
        # https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file
        # print(*words, sep=", ")

        for matched_words in words:
            collections[matched_words] += 1
    return collections


if __name__ == "__main__":
    # given = input("Please entry file and words in the following format:\n  filename words1 words2...\n").strip()
    # file, *words_tuple = given.strip().split()
    curr_dir = os.getcwd()
    # print(__file__ + "\n")

    file = "ex18_input.txt"
    words_tuple = ["asdf", "3"]

    print(words_count(file, words_tuple))     # output is: defaultdict(<class 'int'>, {'asdf': 1, '3': 2})
