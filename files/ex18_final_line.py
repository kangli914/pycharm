#!/usr/bin/env python3

"""Print the last line of the file."""

import os

file = "apache.log"
path = os.getcwd()


# 1) read from lines
with open(f"{path}/dicts/{file}", "r") as reader:
    # print("{0:20} {1}".format( f"last line #: {len(reader.readlines())}", reader.readlines() ))
    for line in reader.readlines():
        '''
        each line already ends with a newline character. This can
        lead to doubled whitespace between printed output. The solution is to stop print
        from displaying anything by overriding the default \n value in the end parameter. By
        passing end='' , we tell print to add '' , the empty string, after printing final_line
        '''
        print(line, end="")

print()

# 2) read from file object directly - memory efficient and fast
with open(f"{path}/dicts/{file}", "r") as f:
    # loop over the file object. This is memory efficient and fast
    for line in f:
        print(line, end="")

    # read all the lines of a file in a list
    # list(f) or f.readlines()

print()

with open(f"{path}/dicts/{file}", "r") as f1:
    print(f"last line:\n {f1.readlines()[-1]}")


with open(f"{path}/dicts/{file}", "r") as f2:
    print(f"last line:\n {list(f2)[-1]}")
