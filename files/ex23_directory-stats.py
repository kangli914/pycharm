#!/usr/bin/env python3

"""
Ask the user for the name of a directory. Iterate through each file in that directory (ignoring subdirectories),
getting (via os.stat) the size of the file and when it was last modified. Create a JSON-formatted file on disk
listing each file name, size, and modification timestamp. Then read the file back in, and identify which files
were modified most and least recently, and which files are largest and smallest, in that directory.

entery a direcotry: files
  file ex22_input.txt is smallest in size 20 bytes
  file mini-access-log.txt is largest in size 36562 bytes
  file ex18_input.txt is modified least recently 2022-08-09 09:08:01.688761
  file ex23_directory-stats.py is modified most recently  2022-05-30 09:41:09.439346
"""


import json
import os
import pathlib
import sys
from datetime import datetime


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
    # print(files_dict)

    out_file = root / "ex23_out.json"
    with open_file_safely(out_file, mode="w") as wfile:
        json.dump(files_dict, wfile, sort_keys=True, separators=(",", ": "), indent=4)

    input_file = out_file
    files_final_stats = []
    with open_file_safely(input_file, mode="r") as rfile:
        data = json.load(rfile)

        # min_val = min(data.values())
        # res = [k for k, v in data.items() if v == min_val]

        # https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
        files_final_stats.append(min(data.items(), key=lambda x: x[1][0]))
        files_final_stats.append(max(data.items(), key=lambda x: x[1][0]))
        files_final_stats.append(min(data.items(), key=lambda x: x[1][1]))
        files_final_stats.append(max(data.items(), key=lambda x: x[1][1]))

    print(f"file {files_final_stats[0][0]} is smallest in size {files_final_stats[0][1][0]} bytes")
    print(f"file {files_final_stats[1][0]} is largest in size {files_final_stats[1][1][0]} bytes")
    print(f"file {files_final_stats[2][0]} is modified least recently {datetime.fromtimestamp(files_final_stats[0][1][1])}")
    print(f"file {files_final_stats[3][0]} is modified most recently  {datetime.fromtimestamp(files_final_stats[1][1][1])}")
