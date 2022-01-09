#!/usr/bin/env python3

"""Print line from each file."""

import os
from itertools import zip_longest


def all_files(path):
    """Return a list of files"""
    # return the files as <class 'generator'> with "()" instead of list
    files = (os.path.join(path, f) for f in os.listdir(path) if f.endswith(".csv"))
    return files


def open_file_safely(file):
    """Open file safe"""
    try:
        return open(file)
    except OSError:
        return None


def alternative_lines(files):
    all_files = [open_file_safely(file) for file in files]

    ## solution # 1: using while in a list of all_lists if list is not empty
    # while all_files:
    #     for one_file in all_files:
    #         if one_file is None:
    #             all_files.remove(one_file)
    #             continue
    #
    #         one_line = one_file.readline()
    #
    #         if one_line:
    #             yield one_line
    #         else:
    #             all_files.remove(one_file)

    ## solution # 2: using zip_longest iteratator tool
    print(*all_files)
    # <_io.TextIOWrapper name='../iterators/token.csv' mode='r' encoding='UTF-8'>
    # <_io.TextIOWrapper name='../iterators/results-scrubbed-5VU.csv' mode='r' encoding='UTF-8'>
    # <_io.TextIOWrapper name='../iterators/users.csv' mode='r' encoding='UTF-8'>

    for tuple_line in zip_longest(*all_files):
        for item in tuple_line:
            if item:
                yield item


if __name__ == "__main__":
    print(type(all_files("../iterators")))
    print('\n'.join(all_files("../iterators")))
    print()
    """
    <class 'generator'>
    ../iterators/token.csv
    ../iterators/results-scrubbed-5VU.csv
    ../iterators/users.csv
    """

    files = all_files("../iterators")
    for line in alternative_lines(files):
        print(line, end="")
