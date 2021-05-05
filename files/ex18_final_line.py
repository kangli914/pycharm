#!/usr/bin/env python3

"""Print the last line of the file."""

import os

file = "apache.log"
path = os.getcwd()

with open(f"{path}/dicts/{file}", "r") as reader:
    print("{0:20} {1}".format( f"last line #: {len(reader.readlines())}", reader.readlines() ))
