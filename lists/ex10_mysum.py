#!/usr/bin/env python3

"""My sum.

Redefine the mysum function we defined in chapter 1, such that it can take any number of arguments. The arguments must all be of the
same type and know how to respond to the + operator.If passed no arguments, then return an empty tuple.
"""

# *args is tuple
# see the value of Python’s slices so not worrying about the element type (e.g. int, string and etc)
# slices are forgiving and allow us to specify indexes beyond the sequence’s boundaries.


def mysum(*args):
    # # *args is tuple --> also look at listtuple-defaultdict_zip.py
    # “splat” (*) operator means accept any number of arguments, which are put into the items tuple
    # print(type(args))
    # <class 'tuple'>
    # print(args)
    # ('abc', 'def')
    # ([1, 2, 3], [4, 5, 6])

    # tuple unpacking
    a, *b = args
    print(f"a={a}, b={b}")
    # a=[1, 2, 3], b=[4, 5, 6]

    if not args:
        return args
    first = args[0]
    for element in args[1:]:
        first += element
    return print(first)

    ## having problem with type this way: TypeError: unsupported operand type(s) for +=: 'int' and 'list'    sum += ele
    # sum = None
    # for ele in args[:]:
    #     sum += ele
    # print(sum)


mysum('')
mysum([])
mysum('abc', 'def')
mysum([1, 2, 3], [4, 5, 6])

# slices are forgiving and allow us to specify indexes beyond the sequence’s boundaries.
# in such a case mysum having only 1 element, we’ll just get an empty sequence, over which the for loop will run zero times
mysum(1)

# TypeError: can only concatenate tuple (not "int") to tuple
#mysum((10, 20, 30), 60)

mysum(1+1)
mysum([1, 2, 3] + [4, 5, 6])


mysum([1, 2, 3], [4, 5, 6])