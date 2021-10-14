#!/usr/bin/env python3

"""Take a a list or tuple of numbers. Return a two-element list, containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers."""


def even_odd_sums(data):
    even = 0
    odd = 0
    for i, item in enumerate(data):
        if i % 2:
            even += int(item)
        else:
            odd += int(item)
    return [even, odd]




print(even_odd_sums([1, 3, 2, 7, 2]))
even_odd_sums((1, 3, 2, 7, 2))
