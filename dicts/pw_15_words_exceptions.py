#!/usr/bin/env python3

"""
Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results.
"""

import os
from pathlib import Path


def open_file_safely(file, file_mode="r"):
    try:
        return open(file, mode=file_mode)
    except OSError:
        os.error("problem in open the file {file}.")


def words_length(file):
    word_dict = {}
    with open_file_safely(file) as f:
        for line in f:
            words = line.strip().split(" ")
            for word in words:
                key = len(word)
                try:
                    word_dict[key] += 1
                except KeyError:
                    word_dict[key] = 1
    return word_dict


if __name__ == "__main__":
    dir = Path.cwd()
    input_file = dir / "dicts" / "apache.log"
    results = words_length(input_file)
    for k, v in results.items():
        print(k, v)
