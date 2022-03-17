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
    user_dict = defaultdict(list)

    # str.strip() removes the whitespace—the space character, as well as \n, \r, \t,
    with open_file_safe(os.path.join(cwd_path, "files", "ex18_faked_pd.txt")) as f:

        for line in f:
            # start with can take a tuple ()
            if not line.strip().startswith(('#', '\n')):
                first, second, third, *others = line.strip().split(":")
                user_dict[first] = third

    # for k, v in user_dict.items():
    #     print(k, v)

    print(user_dict.items())
