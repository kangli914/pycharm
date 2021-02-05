#!/usr/bin/env python3

"""Diff two dictionaries.

Takes two dicts as arguments. The function returns a new dict that expresses the difference between the two dicts
"""

d1 = {"a": 1, "b": 2, "c": 3}
d2 = dict(a=1, b=2, c=4)
d3 = dict([("a", 1), ("b", 2), ("d", 3)])
d4 = dict(a=1, b=2, c=4)
d5 = dict([("a", 1), ("b", 2), ("d", 4)])


def dictdiff(first: dict, second: dict):
    """Diff two given dictionary output the difference."""
    output = dict()

    for k1 in first.keys():
        v1 = first.get(k1)
        v2 = second.get(k1)

        # key exists in first but not second
        if not v2:
            output[k1] = [v1, None]
        # key exists in both first and second
        else:
            # same key but values are different
            if v1 != v2:
                output[k1] = [v1, v2]

    for k2 in second.keys():
        v1 = first.get(k2)
        v2 = second.get(k2)

        # key exists in second but not first
        if not v1:
            output[k2] = [None, v2]

        ## repeated as it was done in previous forloop
        # key exists in both first and second
        # else:
        #     # same key but values are different
        #     if v1 != v2:
        #         output[k1] = [v1, v2]

    return output


print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d3, d4))
print(dictdiff(d1, d5))
