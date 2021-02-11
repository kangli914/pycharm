#!/usr/bin/env python3

"""Python dictionary to combine more dictionary to one.

It takes any number of dicts and returns a dict that reflects the combination of all of them.
If the same key appears in more than one dict, then the most recently merged dict’s value should appear in the output.
"""

d1 = {"a": 1}
d2 = dict(a=3, b=3, c=4)
d3 = dict([("b", 5), ("d", 6)])


def merge(*args):
    """Take in a number of dictionaries and combine to one."""
    output = dict()
    # join dictionary keys() results a set
    all_keys = set()

    for d in args:
        all_keys = all_keys | d.keys()

    for k in all_keys:
        value = None
        for d in args:
            value = d.get(k)

        # if value:
        output[k] = value

    return output


print(merge(d1, d2))
print(merge(d3, d2))
