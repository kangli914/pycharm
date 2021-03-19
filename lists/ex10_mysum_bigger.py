#!/usr/bin/env python3

"""It takes a first argument that precedes *args.

That argument indicates the threshold for including an argument in the sum.
"""

def mysum_bigger_than(base, *args):

    ## having problem with type: TypeError: unsupported operand type(s) for +=: 'int' and 'str': sum += element for string case:  mysum_bigger_than("c", "a", "b", "c", "d", "e")
    # sum = 0
    # for element in args[:]:
    #     if element >= base:
    #         # print(element)
    #         sum += element
    # print(sum)

    first = args[0]
    first_idx = 0

    # find the first idx and first item which is bigger than base value
    for idx, item in enumerate(args):
        if item >= base:
            first_idx = idx
            first = item
            break

    # print(first)
    # print(args[first_idx+1:])
    for element in args[first_idx + 1:]:
        if element >= base:
            first += element
    print(first)


mysum_bigger_than(30, 5, 20, 30, 6)
mysum_bigger_than("a", "a", "b", "c", "d", "e")
