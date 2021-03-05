#!/usr/bin/env python3

"""My zip implmentation.

It takes any number of iterables and returning a list of tuples. Each tuple
will contain one element from each of the iterables passed to the function.
"""


def myzip(*args):
    """My zip fucntion."""
    my_list = []

    for o_idx, iter in enumerate(args):
        # print(o_idx, iter)

        for i_idex, e in enumerate(iter):
            if len(my_list) == len(iter):
                my_list[i_idex] = my_list[i_idex] + (e,)

            else:
                my_list.insert(i_idex, (e,))

    return my_list


print(myzip([10, 20, 30], 'abc', (1, 2, 3)))
