#!/usr/bin/env python3

"""Use custome my_chain( another itertools module chain() ) function to iterate all the lines of files in a directory.
Reimplement the all_lines function from exercise 48 (ex48_directory_generator.py) using mychain.
"""

import os


def mychain(*args):
    # The function takes *args as a parameter, meaning that args will be a tuple when
    # our function executes.
    for arg in args:
        print(f"**************** file name: {arg}")
        for item in arg:
            yield item


def all_lines(path):
    # for file in [os.path.join(path, filename) for filename in os.listdir(path)]:
    #     try:
    #         with open(file) as f:
    #             for line in f:
    #                 yield line
    #     except OSError:
    #         pass

    files = [open(os.path.join(path, filename)) for filename in os.listdir(path) if filename.endswith(".conf") and os.path.isfile(os.path.join(path, filename))]

    # mychain is expecting a tuple but file is a list so we will need to put star in front to make it become tuple
    # or look at the exmaple in ex50_mychain.py how to pass as a tuple than a list:
    #                                   for item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
    return mychain(*files)


if __name__ == "__main__":
    dir = '/etc/'
    for line in all_lines(dir):
        print(line)
