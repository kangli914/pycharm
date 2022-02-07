#!/usr/bin/env python3


"""ex 50 generator function can iterate a set of collections"""

# One of my favorite objects in itertools is called chain. It takes any number of iterables as arguments and then returns each of their elements, one at a time,
# as if they were all part of a single iterable

# best way is to use itertools
"""
from itertools import chain
for one_item in chain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)
"""

''' old
def chain(*args):
    # print(type(args)) 
    for arg in args:
        for item in arg:
            yield item

for one_item in chain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)
'''


def mychain(*data_sets):
# The function takes *args as a parameter, meaning that args will be a tuple when
# our function executes. since it’s a tuple, we can iterate over its elements, no matter
# how many there might be

    # for data in data_sets:
    #     for item in data:
    #         yield(item)

    # *Generator Expression* implementation below:
    # - Generator expressions uses round parentheses "()" vs. list comprehensions uses  squares brackets "[]"
    # - Generator expressions returns one element at a time vs. list comprehension returns lists that comsume more memory
    # also use better than double for loop

    return (item for one_set in data_sets
                 for item in one_set)


if __name__ == "__main__":
    for item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
        print(item)
