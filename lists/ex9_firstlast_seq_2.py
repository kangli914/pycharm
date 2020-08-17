#!/usr/bin/env python3

"""a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of
the odd-indexed numbers
"""

def even_odd_sums(seq, **kwargs):
    odd = 0
    even = 0
    for i in seq[::2]:
        odd += int(i)
    for j in seq[1::2]:
        even += int(j)
    return odd, even



if __name__ == "__main__":
    sum = even_odd_sums([10, 20, 30, 40, 50, 60])
    print(sum, type(sum))