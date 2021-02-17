#!/usr/bin/env python3

import os

"""Set practice: Read through a apache server log file and find out the what were the different IP addresses that tried to access your server.

reference: https://www.programiz.com/python-programming/set

- set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
- set operations like union, intersection, symmetric difference, etc.
- set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements. (e.g. set can not have a list as element resulting 'unhashble type list error')

operation:
- add(): add a single element.
- update(): which takes an iterable as an argument so it can take tuples, lists, strings or other sets as its argument.
- discard(): leaves a set unchanged if the element is not present in the set.
- remove(): aise an KeyError error if element is not present in the set.
"""

path = os.getcwd()

ip_set = set()
with open(f"{path}/dicts/apache.log", "r") as f:
    for line in f.readlines():
        ip = line.strip().split()[0]
        ip_set.add(ip)

print(ip_set)
