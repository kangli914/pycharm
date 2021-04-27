#!/usr/bin/env python3

"""Given a sequence of positive and negative numbers, sort them by absolute value."""

'''
Sorted() function by key:
the key parameter to sorted: The value passed to that parameter(key=) must be a function that takes a single argument. The function will be invoked once per element, and the function’s return value will be used
to sort the values.

Lambda:
1- To create an anonymous function with lambda, use the reserved world Lambda
2- then list any parameters before a colon.(e.g. x below)
3- Then write the one-line expression that the lambda returns.
'''


def abs_helper(number):
    """This helper function will be invoked once per element (a number) in the sequence"""
    return abs(number)


def sort_by_absolute_using_helper(seq):
    print(sorted(seq, key=abs_helper))


def sort_by_absolute_using_lambda(seq):
    """Sort by value."""
    print(sorted(seq, key=lambda x: abs(x)))

seq = (1, 0, -3, -2, 4, -9)


sort_by_absolute_using_helper(seq)
# using lambada to save write extra helper fucntion
sort_by_absolute_using_lambda(seq)
