#!/usr/bin/env python3

"""Find the longest words from each file givne a direcotry.

find_longest_word takes a filename as an argument and returns the longest word found in the file.
find_all_longest_words takes file lists objects and returns a dict in which the keys are filenames and the values are the longest words from each file.
"""

import os
import sys
from glob import glob


def open_file_safe(file):
    """Open the file saftly.

    Accept a filename as an arugment. It throws the errors and exits if having error.
    """
    try:
        return open(file)
    except FileNotFoundError:
        raise OSError(f"file {file} was not found!")


def find_longest_word(file_obj):
    """Take a filename object as an argument and returns the longest word found in the file."""
    longest_word = ""

    for line in file_obj:
        for words in line.strip().split():
            if len(words) > len(longest_word):
                longest_word = words

    return longest_word


def find_all_longest_words(files_objs):
    """Find the longest word from a file and return a dictionary with file name and longest words in that file."""
    longest_words_dict = dict()

    for file_obj in files_objs:
        with file_obj as f:
            longest_word = find_longest_word(f)

        # get file name from the file object or so called file pointer f.name
        file_name = file_obj.name.split('/')[-1]
        print(f"The longest word in ( {file_name} ) is ( {longest_word} )")
        longest_words_dict[file_name] = longest_word

    return longest_words_dict
    # another good implementation

if __name__ == "__main__":
    path = os.getcwd()
    path = os.path.join(path, "files")

    # glob returns a list of file objects
    files = [open_file_safe(file) for file in glob(f'{path}/*.txt', recursive=True)]
    print(find_all_longest_words(files))
