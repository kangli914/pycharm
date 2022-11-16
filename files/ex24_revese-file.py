#!/usr/bin/env python3

"""Rerverse the text in the file. """

import os
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely and return the file wrapper when no error."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error(f"having issue opening the file {file}!")


if __name__ == "__main__":

    # /home/kangli/repo/personal/pycharm
    # root_path = Path.cwd()
    # /home/kangli/repo/personal/pycharm/files
    # path = root_path / "files"

    path = Path("files")
    rfile = path / "ex18_vowel.txt"
    wfile = path / "ex24_out.txt"
    with open_file_safely(rfile) as reader, open_file_safely(wfile, mode="w") as writer:
        for line in reader:
            reversed = line.rstrip()[::-1]
            writer.write(f"{reversed}\n")
