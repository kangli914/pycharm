#!/usr/bin/eny python3

"""Find directory file extensions(suffixes)."""

import os

dir_path = os.getcwd()
ext_set = set()

for item in os.listdir(f"{dir_path}/dicts"):

    ## split() split dict and file to a tuple pair
    # print(os.path.split(f"{dir_path}/dicts/{item}"))

    ## split() split dict/file_name and file extension to a tuple pair
    # print(os.path.splitext(f"{dir_path}/dicts/{item}"))

    ext_set.add(os.path.splitext(item)[1])

print(ext_set)
## output:
## {'.log', '.py'}