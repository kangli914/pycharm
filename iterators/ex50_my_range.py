#!/usr/bin/env python3


"""Implement custom range() funtion using generator expression."""

'''
Generator expressions vs. List comprehensions:
generator expressions look and work similarly to list comprehensions, except that you use round parentheses rather than square brackets

- Generator expressions uses round parentheses "()" vs. list comprehensions uses  squares brackets "[]"
- Generator expressions returns one element at a time vs. list comprehension returns lists that comsume more memory
- A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again.
- However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausted when you complete iterating over it.

# good refernece: generator fucntion vs generator expression:
# https://www.pythontutorial.net/advanced-python/python-generator-expressions/
- Generator expression is an expression that returns a generator object.
- Generator function is a function that contains a yield statement and returns a generator object
Because a generator object is an iterator, you can use a for loop to iterate over its elements
A generator expression provides you with a more simple way to return a generator object.
'''

'''
Syntax:
native function: range(start, stop, step):
start (Optional). An integer number specifying at which position to start. Default is 0
stop (Required). An integer number specifying at which position to stop (not included).
step (Optional). An integer number specifying the incrementation. Default is 1
'''
def range_in_generator_expression(start, stop=None, step=1):
    if not stop:
        current = 0
        stop = start
    else:
        current = start
        # stop = stop

    while current < stop:
        yield current
        current += step


if __name__ == "__main__":
    for item in range_in_generator_expression(2, 6, 2):
        print(item)

    print("-------------")
    for item in range_in_generator_expression(6):
        print(item)
