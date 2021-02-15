#!/usr/bin/env python3

"""Split a dictionary to two based on a fucntion.

Takes one dict (d) and a function (f) asarguments. dict_partition will return two dicts, each containing key-value
pairs from d.
The decision regarding where to put each of the key-value pairs will be made according to the output from f , which will be run on each key-value pair in d. If f returns True, then the key-value pair will be put in the first output dict. If f returns False , then the key-value pair will be put in the second output dict.
"""


def spliter(data):
    t = []
    for idx, item in enumerate(data, 1):
        if idx % 2:
            t.append(True)
        else:
            t.append(False)
    return t


def dict_partition(d, func):
    """Split given dictionary based on the fucntion f."""

    d1 = {}
    d2 = {}
    outcome = func(d)

    for pair, out in zip(d.items(), outcome):
        if out:
            d1[pair[0]] = pair[1]
        else:
            d2[pair[0]] = pair[1]
    return d1, d2


d = dict([("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5), ("f", 6)])
a, b = dict_partition(d, spliter)
print(a, b)
