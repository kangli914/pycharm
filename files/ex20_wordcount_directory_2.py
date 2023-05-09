#!/usr/bin/env python3

"""Given a directory, read through each file and count the frequency of each let-
ter. (Force letters to be lowercase, and ignore non letter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files."""


from pathlib import Path
from collections import Counter


def open_file_safely(file, mode="r"):
    """Open a given file safely and raise an error if having a problem."""

    try:
        return open(file, mode=mode)
    except FileNotFoundError:
        raise OSError(f"file {file} was not found!")


def count_letter_frequencies(word_counter, file):
    """Count the frequencies of the letters in a given file."""

    # words_list = []
    with open_file_safely(file) as f:
        print(f"processing file {file}")

        # for line in f:
        #     for words in line.strip().split():
        #         words_list.append(words)
        words_list = [words.lower() for line in f for words in line.strip().split()]
    word_counter.update(words_list)


if __name__ == "__main__":

    dict_count = Counter()
    input_dir = input("Eneter a directory: ")

    path = Path(input_dir)
    for child in path.iterdir():
        if child.is_file():
            count_letter_frequencies(dict_count, child)

    print(dict_count.most_common(5))
