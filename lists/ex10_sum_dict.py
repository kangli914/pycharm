#!/usr/bin/env python3

"""A function that takes a list of dicts and returns a single dict that combines all of the keys and values.

If a key appears in more than one argument, the value should be a list containing all of the values from the arguments.
"""

# from collections import defaultdict

def dict_combine(*args):
    # print(type(args))
    # print(args)
    # for i in args:
    #     print(i)

    output = dict()
    all_keys = set()
    for d in args:
        all_keys = all_keys | d.keys()

    for k in all_keys:
        
        for item in args:
            value = d.get(k)
            if value:
                output[k] = value

    print(output)

d1 = dict(tea=1, tandwitch="12", burger=20)
d2 = dict([("tea", "1"), ("noodle", "3")])
dict_combine(d1, d2)
