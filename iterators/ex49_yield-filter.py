#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49, beyond 3: yield_filter

Write a generator function that takes two elements: an iterable and a function.
With each iteration, the function is invoked on the current element. If the
result is True, then the element is returned as is. Otherwise, the next element is
tested, until the function returns True.
"""

def my_func(one):
    return one


def yield_filter(data, func):
    for one_item in data:
        # if my_func return a value. e.g. one_item = "a", the following if statement will be evaludate as true
        # one_item = "a", then assert(one_item) == True
        if func(one_item):
            yield one_item


if __name__ == "__main__":
    for item in yield_filter("abcde", my_func):
        print(item)
