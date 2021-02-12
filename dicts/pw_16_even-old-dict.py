#!/usr/bin/env python3

"""Python dictionary to reform based on the given argument.

The even-indexed arguments become the dict keys, while the odd-numbered arguments become the dict values.
Thus, calling the function with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being returned.
"""


def dict_reform(orig_dict):
    """Given a tuple it takes even-indexed arguments become the dict keys while the odd-numbered arguments become the dict values."""
    output = dict()

    key = None
    for idx, item in enumerate(orig_dict):
        if not idx % 2:
            output.setdefault(item, None)
            key = item
        else:
            output[key] = item
    return output


a = ("a", 1, "b", 2, "c", 3)
print(dict_reform(a))
