#!/usr/bin/env python3

# Generator expressions:
'''
Generator expressions vs. List comprehensions:
generator expressions look and work similarly to list comprehensions, except that you use round parentheses rather than square brackets

- Generator expressions uses round parentheses "()" vs. list comprehensions uses  squares brackets "[]"
- Generator expressions returns one element at a time vs. list comprehension returns lists that comsume more memory

There are 3 ways to create iteratble objects:
1 We’ll create our own iterators via Python classes, directly implementing the
protocol ourselves.
2 We’ll create generators, objects that implement the protocol, based on some-
thing that looks very similar to a function. Not surprisingly, these are known
as generator functions.
3 We’ll also create generators using generator expressions, which look quite a bit
like list comprehensions.
'''

def foo():
    things = ["a", "b", "c"]
    return (item for item in things)

for one_item in foo():
    print(one_item)

print(type(foo()))

'''

'''
