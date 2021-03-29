#!/usr/bin/env python3

"""Create a list of tuple using zip and mixed with default dictionary.

- given a list and a tuple
- 1) use zip to create a tuple list with new corresponding mapping
- 2) slicing/dicing
- 3) use collection module to covert list of tuple to a dictionary with non-dumplicate tuple:
[('a', 1), ('b', 2), ('c', 3), ('c', 3), ('d', 3)] --> [('a', {1}), ('b', {2}), ('c', {3}), ('d', {3})]
reference:
https://www.askpython.com/python/built-in-methods/python-zip-function
https://www.askpython.com/python/list/python-list-of-tuples
"""


from collections import defaultdict

a_list = ["a", "b", "c", "c", "d"]
b_tuple = (1, 2, 3, 3, 3)

# zip() accepts iterable elements as input and returns an iterable as the output. it aggregates elements from the iterables and returns *iterables* of tuples.
# zip() wraps tow or mroe iterators with a lazy generator, The zip generators yeilds *tuples* containing the next value from each iterator
new_list_tuple = list(zip(a_list, b_tuple))
print(new_list_tuple)
# [('a', 1), ('b', 2), ('c', 3), ('c', 3), ('d', 3)]


# use unpacking to unpack tuple: allow for assigning multiple values in a single statement using (*x)
# unpack a tuple:
a, b, *last = b_tuple
# a=1, b=2, c=[3, 3, 3]

# unpacking a list of tuples using enumerate
for idx, (first, second) in enumerate(new_list_tuple, 1):
    print(f"#{idx}: {first} {second}")
#1: a 1
#2: b 2
#3: c 3
#4: c 3
#5: d 3

## new_list_tuple = [('a', 1), ('b', 2), ('c', 3), ('c', 3), ('d', 3)]

# below unzip a list of tuples and unpacking the first and second elements from a list of tuples
new_first_tuple, new_second_tuple, *last = new_list_tuple
print(f"new_first_tuple = {new_first_tuple}")
print(f"new_second_tuple = {new_second_tuple}")
# new_first_tuple = ('a', 1)
# new_second_tuple = ('b', 2)

# uze zip() and Unpacking Argument Lists (*) to unzip a list of tuple
# https://docs.python.org/3.9/tutorial/controlflow.html#unpacking-argument-lists
# here:
# 1) *new_list_tuple - first unpack list into many tuples iterables
# 2) then use zip using zip generators yeilds each tuples containing the next value from each iterator
new_first_tuple, new_second_tuple = zip(*new_list_tuple)
print(f"new_first_tuple = {new_first_tuple}")
print(f"new_second_tuple = {new_second_tuple}")
# new_first_tuple = ('a', 'b', 'c', 'c', 'd')
# new_second_tuple = (1, 2, 3, 3, 3)

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




# more to think of with zip and why?
a_list = ["a", "b", "c", "c", "d"]
print(list(zip(a_list)))
# [('a',), ('b',), ('c',), ('c',), ('d',)]
print(list(zip(*a_list)))
#  *-operator to unpack the arguments out of a list or tuple? according to https://docs.python.org/3.9/tutorial/controlflow.html#unpacking-argument-lists
# [('a', 'b', 'c', 'c', 'd')]
