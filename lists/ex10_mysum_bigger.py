#!/usr/bin/env python3

"""It takes a first argument that precedes *args.

That argument indicates the threshold for including an argument in the sum.
"""


def mysum_bigger_than(base, *args):

    ## having problem with type: TypeError: unsupported operand type(s) for +=: 'int' and 'str': sum += element
    # sum = 0
    # for element in args[:]:
    #     if element >= base:
    #         # print(element)
    #         sum += element
    # print(sum)

    first = args[0]
    # if first < base:
    #     new_args = args[1:]
    #     print(args)
    #     first = args[1]
    # if first < base:
    #     first = first - first

    # print(first)
    for element in args[1:]:
        if element >= base:
            first += element
    print(first)


mysum_bigger_than(10, 5, 20, 30, 6)
mysum_bigger_than("c", "a", "b", "c", "d", "e")
