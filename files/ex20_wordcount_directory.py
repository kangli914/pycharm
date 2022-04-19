#!/usr/bin/env python3

"""Given a directory, read through each file and count the frequency of each letter.

Force letters to be lowercase, and ignore nonletter characters, and find the five most common letters
across all of these files.
"""

import os
from re import L
import sys
from collections import defaultdict

from collections import Counter
import glob


def open_file_safely(file):
    """Open the file saftly.

    Accept a filename as an arugment. It throws the errors and exits if having error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encoutnered in open the file {file}")


def all_files(path):
    """Return a generator of a list of file TextIO objects in the given directory."""
    files_obj_list = (open_file_safely(os.path.join(path, filename)) for filename in os.listdir(path) if filename.endswith(".txt") and os.path.isfile(os.path.join(path, filename)))

    print(type(files_obj_list))  # <class 'generator'>
    """
    <_io.TextIOWrapper name='/home/kangli/repo/personal/pycharm/files/ex18_2-cols-numbers.txt' mode='r' encoding='UTF-8'>
    <_io.TextIOWrapper name='/home/kangli/repo/personal/pycharm/files/ex18_faked_pd.txt' mode='r' encoding='UTF-8'>
    <_io.TextIOWrapper name='/home/kangli/repo/personal/pycharm/files/ex18_input.txt' mode='r' encoding='UTF-8'>
    <_io.TextIOWrapper name='/home/kangli/repo/personal/pycharm/files/ex18_vowel.txt' mode='r' encoding='UTF-8'>
    <_io.TextIOWrapper name='/home/kangli/repo/personal/pycharm/files/ex20_wordcounts_input.txt' mode='r' encoding='UTF-8'>
    """

    return files_obj_list


def all_lines(files):
    """Yeild one line at a time from a generator fucntion."""
    for f in files:
        print(f'------------------- file name: {f} -------------------')
        for line in f:
            yield line


def words_in_line(line, collections):
    """Return a collections of words given a line."""
    # for a_words in line.strip().split():
    #     collections[a_words] += 1

    # use Generator Expressions here!! (look for ex20_words-in-file_generator-expression.py)
    letters = (letter for a_words in line.strip().split() for letter in a_words)
    for one_letter in letters:
        collections[one_letter.lower()] += 1

    return collections


# another implmentation using glob and counter
def most_common_letters(dirname):
    counts = Counter()

    for one_filename in glob.glob(f'{dirname}/*.txt', recursive=True):
        try:
            for one_line in open(one_filename):
                counts.update(one_line.lower())
        except:
            pass

    return list(dict(counts.most_common(5)).items())


if __name__ == "__main__":
    path = os.getcwd()
    collections = defaultdict(int)
    files = all_files(os.path.join(path, "files"))
    for line in all_lines(files):
        # print(line)
        words_in_line(line, collections)

    # for k, v in collections.items():
    #     print(f"{k, v}")
    top_five = sorted(collections, key=collections.get, reverse=True)[:5]
    print("- top 5 -")
    for key in top_five:
        print(f"key: {key}, occurrence: {collections.get(key)}")

    print(most_common_letters(f"{path}/files"))
