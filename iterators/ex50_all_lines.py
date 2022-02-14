#!/usr/bin/env python3

"""Use custome my_chain( another itertools module chain() ) function to iterate all the lines of files in a directory.
Reimplement the all_lines function from exercise 48 using mychain.
"""

import os


def mychain(*args):
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
    return mychain(*files)


if __name__ == "__main__":
    dir = '/etc/'
    for line in all_lines(dir):
        print(line)
