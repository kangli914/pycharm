#!/usr/bin/env python3

# Generator expressions:
'''
Generator expressions vs. List comprehensions:
generator expressions look and work similarly to list comprehensions, except that you use round parentheses rather than square brackets

- Generator expressions uses round parentheses "()" vs. list comprehensions uses  squares brackets "[]"
- Generator expressions returns one element at a time vs. list comprehension returns lists that comsume more memory
- A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again.
- However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausted when you complete iterating over it.

There are 3 ways to create iteratble objects:
1 We’ll create our own iterators via Python classes, directly implementing the
protocol ourselves.
2 We’ll create generators, objects that implement the protocol, based on some-
thing that looks very similar to a function. Not surprisingly, these are known
as generator functions.
3 We’ll also create generators using generator expressions, which look quite a bit
like list comprehensions.
'''

# good refernece: generator fucntion vs generator expression:
# # # https://www.pythontutorial.net/advanced-python/python-generator-expressions/
# - Generator expression is an expression that returns a generator object.
# - Generator function is a function that contains a yield statement and returns a generator object

def foo():
    things = ["a", "b", "c"]
    return (item for item in things)

for one_item in foo():
    print(one_item)

print(type(foo()))

'''

'''
