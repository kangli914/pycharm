#!/usr/bin/env python3

"""Alternate plus and minus."""


def plus_minus(seq):
    """Take a list or tuple of numbers.

return the result of alter-nately adding and subtracting numbers from each other.
"""
    even = 0
    for i in seq[1::2]:
        even += i
        print(even)

    odd = seq[0]
    for i in seq[2::2]:
        odd -= i
        print(odd)

    return even + odd


print(plus_minus([10, 20, 30, 40, 50, 60]))
