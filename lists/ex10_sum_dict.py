#!/usr/bin/env python3

"""A function that takes a list of dicts and returns a single dict that combines all of the keys and values.

If a key appears in more than one argument, the value should be a list containing all of the values from the arguments.
Also, use collection module (defaultdict) to covert list of tuples to a dictionary with non-dumplicate tuple: tuple --> dictionary
"""

from collections import defaultdict

def dict_combine(*args):
    print(type(args))

    print(" ---- ")
    for idx, item in enumerate(args, 1):
        print(f"arg #{idx}: {item}")
    print(" ---- ")

    # args is <class 'tuple'>
    #---- 
    #arg #1: {'tea': 1, 'tandwitch': '12', 'burger': 20, 'noodle': 3}
    #arg #2: {'tea': '1', 'noodle': '3', 'burger': 40}
    #---- 

    output_list = defaultdict(list)
    output_set = defaultdict(set)

    all_keys = set()
    for d in args:
        all_keys = all_keys | d.keys()

    for k in all_keys:

        for d in args:

            value = d.get(k)

            if value:
                output_list[k].append(value)
                output_set[k].add(value)

    print(output_list)
    print(output_set)
    #---- 
    #defaultdict(<class 'list'>, {'burger': [20, 40], 'tea': [1, '1'], 'noodle': [3, '3'], 'tandwitch': ['12']})
    #defaultdict(<class 'set'>, {'burger': {40, 20}, 'tea': {1, '1'}, 'noodle': {3, '3'}, 'tandwitch': {'12'}})

d1 = dict(tea=1, tandwitch="12", burger=20, noodle=3)
d2 = dict([("tea", "1"), ("noodle", "3"), ("burger", 40)])
dict_combine(d1, d2)
