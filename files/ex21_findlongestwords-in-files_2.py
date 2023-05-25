#!/usr/bin/env python3

"""
Write two functions. find_longest_word takes a filename as an argument and returns the longest word found in the file. The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file.
"""

from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        raise OSError(f"file {file} was not found!")


def find_longest_word(file):
    """Find the longest word in a given file."""
    longest_word = ""
    ''' option 1
    for line in file_obj:
        for words in line.strip().split():
            if len(words) > len(longest_word):
                longest_word = words
    '''

    # option 2 - Using list comprehensions to pull all the words in a file in a set
    # as set will elimite the duplicates
    words_set = {words for line in open_file_safely(file)
                 for words in line.strip("\n\t .").split()}
    # then sort the sets in reversed order
    longest_word = sorted(words_set, key=len, reverse=True)[:1][0]
    return longest_word


def find_all_longest_words(dir):
    """It returns a dict in which the keys are filenames and the values are the longest words from each file"""

    '''
    # long version
    files_dict = {}
    for item in dir.iterdir():
        if item.is_file():
            # return find_longest_word(dir / item)
            key = item.name
            value = find_longest_word(dir / item)
            files_dict[key] = value
    return files_dict
    '''

    # short version
    return {item.name: find_longest_word(dir / item) for item in dir.iterdir() if item.is_file()}


if __name__ == "__main__":
    dir_path = Path.cwd()
    print(find_all_longest_words(dir_path / "files/tmp"))
