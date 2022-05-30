#!/usr/bin/env python3

"""Convert pw files into a dictionary where the dict’s keys are usernames and the values are the users’ IDs."""

import os
import sys
from collections import defaultdict


def open_file_safe(file):
    """Open file safe."""
    try:
        return open(file)
    except OSError:
        sys.exit(f"error in opening the file {file}")


if __name__ == "__main__":
    cwd_path = os.getcwd()
    print(__file__ + "\n")
    print(os.path.dirname(__file__))
    user_dict = defaultdict(list)

    # str.strip() removes the whitespace—the space character(=such as spaces, tabs, and newlines.), as well as \n, \r, \t,
    with open_file_safe(os.path.join(cwd_path, "files", "ex18_faked_pd.txt")) as f:

        for line in f:

            # or continue
            # if one_line.startswith(('#', '\n')):
            #     continue

            # start() with can take a tuple ()
            if not line.strip().startswith(('#', '\n')):
                first, second, third, *others = line.strip().split(":")
                # str.strip() removes the whitespace—the space character, as well as \n, \r, \t

                # str.split() without any arguments, which causes it to use *all* whitespace (spaces, tabs, and newlines) as delimiters. e.g. the default separator is any whitespace.

                ## not:
                # user_dict[first] = third
                user_dict[first].append(third)

    for k, v in user_dict.items():
        print(k, v[0])

    # print(user_dict.items())
