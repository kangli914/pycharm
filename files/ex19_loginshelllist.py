#!/usr/bin/env python3

"""Returns a dictionary."""


import os
from collections import defaultdict
from pathlib import Path


def open_file_safely(file, mode="r"):
    try:
        return open(file, mode=mode)
    except OSError:
        os.error("problem with openning the file {file}!")


def login_shells(file):
    login_list = defaultdict(list)
    with open_file_safely(file) as f:
        for line in f:
            if not line.startswith(("#", "\n")):
                value, *middle, key = line.strip().split(":")
                login_list[key].append(value)
    return login_list


if __name__ == "__main__":
    directory = Path("/etc")
    file = "passwd"
    file_path = directory / file
    for k, v in login_shells(file_path).items():
        print(k, v)
