#!/usr/bin/env python3

"""Ask the user to enter the name of a text file and then (on one line, separated by
spaces) words whose frequencies should be counted in that file. Count how
many times those words appear in a dict, using the user-entered words as the
keys and the counts as the values.
"""

from collections import Counter, defaultdict
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely."""

    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        '''The issue is with the open_file_safely function. The function is not raising an exception when the file does not exist. Instead, it is returning None, and then the with statement is trying to call the __enter__ method on None, which raises the AttributeError: __enter__ error.
        '''
        # os.error(f"something wrong opening the file {file}!")

        '''With this modification, if the file does not exist, the open function will raise a FileNotFoundError exception, which will be caught by the except block and raised as an OSError exception with a custom error message. This will ensure that the with statement is not called with a None object.
        '''
        raise OSError(f"File not found: {file}")


def count_words(file, input_words):
    """Return a dictionary with word and their count"""

    count = defaultdict(int)
    with open_file_safely(file) as f:
        for line in f:
            list_words_per_line = line.strip().split()
            for word in input_words:
                if word in list_words_per_line:
                    count[word] += 1
    return count


def count_words_2(file, input_words):
    """Instead of looping through the input words and checking if each word is in the list of words per line, you can use a list comprehension to create a list of all the words in the file that match the input words, and then count the frequency of each word in that list using the collections.Counter class."""
    count = dict()
    with open_file_safely(file) as f:
        words_in_file = [word for line in f
                              for word in line.strip().split() if word in input_words]
        count.update(Counter(words_in_file))
    return count


if __name__ == "__main__":
    file, *words = input("file[space]word[space]words...\n").strip().split(" ")
    dir = Path.cwd()
    full_path_file = dir / file
    dict = count_words_2(full_path_file, words)
    for k, v in dict.items():
        print(k, v)
