#!/usr/bin/env python3

"""Given a sequence of positive and negative numbers, sort them by absolute value."""


def sort_by_absolute(seq):
    """Sort by value."""
    print(sorted(seq, key=lambda x: abs(x)))

seq = (1, 0, -3, -2, 4, -9)
sort_by_absolute(seq)
