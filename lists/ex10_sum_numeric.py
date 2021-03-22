#!/usr/sbin/env python3

"""Sum up any integeter values including string type.

Takes any number of arguments. If the argument is or can be turned into an integer, then it should be added to the
total. Arguments that can’t be handled as integers should be ignored. Notice that even if the string 30 is an element in the
list, it’s converted into an integer and added to the total.
"""


def sum_numeric(*args):
    # for item in args:
    #     print(item)

    sum = 0
    for i in args[:]:
        if isinstance(i, str) and i.isnumeric():
            sum += int(i)
        elif isinstance(i, int):
            sum += i

    print(sum)


sum_numeric(10, 20, 'a', '30', 'bcd')
