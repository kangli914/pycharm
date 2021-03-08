#!/usr/bin/env python3

"""My sum.

Redefine the mysum function we defined in chapter 1, such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operato.
"""

# *args is tuple
# see the value of Python’s slices so not worrying about the element type (e.g. int, string and etc)
# slices are forgiving and allow us to specify indexes beyond the sequence’s boundaries.

def mysum(*args):
    if not args:
        return args
    first = args[0]
    for element in args[1:]:
        first += element
    return print(first)


mysum('')
mysum([])
mysum('abc', 'def')
mysum([1, 2, 3], [4, 5, 6])

# slices are forgiving and allow us to specify indexes beyond the sequence’s boundaries.
# in such a case mysum having only 1 element, we’ll just get an empty sequence, over which the for loop will run zero times
mysum(1)
