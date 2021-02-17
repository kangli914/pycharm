#!/usr/bin/env python3

"""A function takes a single list of integers and returns the number of different integers it contains.

Look for set() references in pw_17_readfile.py.
"""

def how_many_different_numbers(data):

    # option 1
    print(set(data))
    print(len(set(data)))

    # option 2
    unique_numbers = set()
    # set.update(), which takes an iterable as an argument
    unique_numbers.update(data)
    print(unique_numbers)

    # option 3
    # tells Python that it should take the elements of numbers and feed them (in a sort of for loop) to the curly brace
    unique_numbers_1 = {*data}
    print(unique_numbers_1)


numbers = [1, 2, 3, 1, 2, 3, 4, 1]
how_many_different_numbers(numbers)
