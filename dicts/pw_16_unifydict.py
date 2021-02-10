#!/usr/bin/env python3

"""Python dictionary to combine more dictionary to one.

It takes any number of dicts and returns a dict that reflects the combination of all of them.
If the same key appears in more than one dict, then the most recently merged
dict’s value should appear in the output.
"""

d1 = {"a": 1}
d2 = dict(a=3, b=3, c=4)
d3 = dict([("b", 5), ("d", 6)])


def merge(*args):
    """Take in a number of dictionaries and combine to one."""
    for d in args:
        



merge(d1, d2)