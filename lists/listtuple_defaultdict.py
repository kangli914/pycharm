#!/usr/bin/env python3

"""Create a list of tuple using zip and mixed with default dictionary.

reference:
https://www.askpython.com/python/built-in-methods/python-zip-function
https://www.askpython.com/python/list/python-list-of-tuples
"""


from collections import defaultdict

a_list = ["a", "b", "c", "c", "d"]
b_tuple = (1, 2, 3, 3, 3)

# zip()  accepts iterable elements as input and returns an iterable as the output. it aggregates elements from the iterables and returns *iterables* of tuples.
new_list_tuple = list(zip(a_list, b_tuple))
print(new_list_tuple)
# [('a', 1), ('b', 2), ('c', 3), ('c', 3), ('d', 3)]

# convert above list of tuples to defaultdictionary as the key from the a_list
d1 = defaultdict(list)
for k, v in new_list_tuple:
    d1[k].append(v)
print(d1.items())
# dict_items([('a', [1]), ('b', [2]), ('c', [3, 3]), ('d', [3])])

d2 = defaultdict(set)
for k, v in new_list_tuple:
    d2[k].add(v)
print(d2.items())
# set automatically elimated the duplicates
# dict_items([('a', {1}), ('b', {2}), ('c', {3}), ('d', {3})])
