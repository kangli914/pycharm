#!/usr/bin/env python3

"""
Ask the user for the name of a directory. Iterate through each file in that directory (ignoring subdirectories),
getting (via os.stat) the size of the file and when it was last modified. Create a JSON-formatted file on disk
listing each file name, size, and modification timestamp. Then read the file back in, and identify which files
were modified most and least recently, and which files are largest and smallest, in that directory.
"""


import json
import os
import pathlib
import sys


def open_file_safely(file, mode="r"):
    """Open file safely and return the file wrapper when no error."""

    try:
        return open(file, mode)
    except OSError:
        os.error("Error encountered when openning the file {file}!")


if __name__ == "__main__":

    files_dict = dict()
    input_dir = input("entery a direcotry: ").strip()

    root = pathlib.Path(input_dir)

    if not root.is_dir():
        print(f"User given {input_dir} is not a direcotry!")
        sys.exit(1)

    # iterdir() only iterate the current level do not recursively iterate.
    # For recusive iteration using https://stackoverflow.com/questions/50714469/recursively-iterate-through-all-subdirectories-using-pathlib
    # e.g. for i in p.glob('**/*'):
    for child in root.iterdir():
        # try:
        #     files_dict[child.name].append(os.stat(child)["st_size="])
        # except KeyError:
        #     files_dict[child.name] = []
        files_dict[child.name] = [os.stat(child).st_size, os.stat(child).st_mtime]
    print(files_dict)

    out_file = root / "ex23_out.json"
    with open_file_safely(out_file, mode="w") as wfile:
        # json.dump(out_file)
        json.dump(files_dict, wfile, sort_keys=True, separators=(",", ": "), indent=4)

