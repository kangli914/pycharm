#!/usr/bin/env python3

"""A simple words count to mimics to the wc to count the charactor, words, unique words and line in the give file."""

import os
import sys


def open_file_safely(file):
    """Open the file safely.

    Accepts a filename as an argument. It throws the errors and exits
    if having the error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"erorr in open the file {file}")


if __name__ == "__main__":
    cwd_path = os.getcwd()
    print(__file__ + "\n")

    wc_dict = {"lines": 0,
               "words": 0,
               "chars": 0}

    unique_wd = set()

    with open_file_safely(os.path.join(cwd_path, "files", "ex20_wordcounts_input.txt")) as f:
        for ln in f:
            wc_dict["lines"] += 1

            # To get the number of characters in the current line by calculating len(one_line)
            # This will count whitespace characters, such as spaces, tabs, and newlines.
            wc_dict["chars"] += len(ln)

            # str.split() without any arguments, which causes it to use *all* whitespace (=spaces, tabs, and newlines) as delimiters. e.g. the default separator is any whitespace

            # option 1 - not efficient as it iterate the line to find the words
            # for wd in ln.strip().split():
            #     wc_dict["words"] += 1
            #     unique_wd.add(wd)

            # option 2 - more efficient to use line.split() to find the words count, and use set.update(iterable) to find the unique word count:
            wc_dict["words"] += len(ln.strip().split())
            unique_wd.update(ln.strip().split())

    wc_dict["unique_word"] = len(unique_wd)

    print(f"lines {wc_dict['lines']}, words {wc_dict['words']}, unique word {wc_dict['unique_word']}, char {wc_dict['chars']}")
