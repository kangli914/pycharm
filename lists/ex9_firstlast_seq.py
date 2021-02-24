#!/usr/bin/env python3

"""Python workout ex9 Write a function, firstlast, that takes a sequence (string, list or tuple) and returns the same type of sequence, but only with two elements — the first and the last from its input."""


def first_last(seq):
    """Given a sequence, returns a two-element sequence.
    The returned sequence will be of the same type as the argument.
    Its two elements will be the argument's first and last elements.
    """
    # access by index would not preserve the seq type e.g.
    # return seq[0] + seq[-1]

    # however, slicing preserve the original type
    return seq[:1] + seq[-1:]

# return seq[0] + seq[-1] will give 6 from below code
print(first_last([1,2,3,4,5]))          # list
print(first_last(("a","b",3,4,5)))      # tuple
print(first_last(("a","b","c")))        # tuple of different type
print(first_last("abc"))                # string
