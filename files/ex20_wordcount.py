#!/usr/bin/env python3

"""
Write a wordcount function that mimics the wc Unix command.
The function will take a filename as input and will print four lines of output.
"""

import os
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error("problem opening the file {file}")


def count(file):
    """Return all the count from the file."""
    count_dict = {"num_char": 0, "num_words": 0, "num_lines": 0, "num_unique_words": 0}
    unique_words = set()
    with open_file_safely(file) as f:
        for line in f:
            count_dict["num_lines"] += 1
            count_dict["num_char"] += len(line)
            # for words in line.strip().split():
            #     count_dict["num_words"] += 1
            #     unique_words.update(words)

            # this save another loop compared to above
            words_list = line.strip().split()
            count_dict["num_words"] += len(words_list)
            # set.update take a collection like a list
            unique_words.update(words_list)

    count_dict["num_unique_words"] = len(unique_words)

    return count_dict


if __name__ == "__main__":
    directory = Path.cwd()
    file_name = "ex20_wordcounts_input.txt"
    print(count(directory / file_name))
