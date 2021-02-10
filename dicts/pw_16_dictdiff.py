#!/usr/bin/env python3

"""Diff two dictionaries.

Use a dict to track how many words of each length are in the file.
That is, how many three-letter words, four-letter words, five-letter words, and so on.
Display your results.

It would be better and smarter for us to collect all of the keys from first and second, put
them into a set (thus ensuring that each appears only once), and then iterate over them.

reference: https://docs.python.org/3/tutorial/datastructures.html
"""

import itertools

d1 = {"a": 1, "b": 2, "c": 3}
d2 = dict(a=1, b=2, c=4)
d3 = dict([("a", 1), ("b", 2), ("d", 3)])
d4 = dict(a=1, b=2, c=4)
d5 = dict([("a", 1), ("b", 2), ("d", 4)])


def dictdiff(first: dict, second: dict):
    """Diff two given dictionaries and output the difference."""
    output = dict()
    key_set = set()

    # add common keys to a set (e.g. a dict without values) using zip() but it will return None
    # same as (union of two keys):
    # first.keys() | second.keys()
    for k1, k2 in itertools.zip_longest(first, second):
        # zip return None if element is not in the set 
        if k1 is not None:
            key_set.add(k1)
        if k2 is not None:
            key_set.add(k2)

    for common in key_set:
        if first.get(common) != second.get(common):
            output[common] = (first.get(common), second.get(common))

    # key in k1 but not in k2:
    for k1 in (first.keys() - second.keys()):
        output[k1] = (first.get(k1), second.get(k1))

    # key in k2 but not in k1:
    for k2 in (second.keys() - first.keys()):
        output[k2] = (first.get(k2), second.get(k2))

    return output


def dictdiff_2(first, second):

    # union of all the keys together with "|"
    new_keys = first.keys() | second.keys()
    output = {}

    for key in new_keys:
        if first.get(key) != second.get(key):
            output[key] = (first.get(key), second.get(key))

    return output


print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d3, d4))
print(dictdiff(d1, d5))

print(dictdiff_2(d1, d1))
print(dictdiff_2(d1, d2))
print(dictdiff_2(d3, d4))
print(dictdiff_2(d1, d5))
