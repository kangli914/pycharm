#!/usr/bin/env python3

"""Solution to chapter 10, exercise 49, beyond 3: yield_filter

Write a generator function that takes two elements: an iterable and a function.
With each iteration, the function is invoked on the current element. If the
result is True, then the element is returned as is. Otherwise, the next element is
tested, until the function returns True.


good refernece: generator fucntion vs generator expression:
https://www.pythontutorial.net/advanced-python/python-generator-expressions/
- Generator expression is an expression that returns a generator object.
- Generator function is a function that contains a yield statement and returns a generator object
- A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again.
- However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausted when you complete iterating over it.
"""

def my_func(one):
    return True


def yield_filter(data, func):
    for one_item in data:
        # if my_func return a value. e.g. one_item = "a", the following if statement will be evaludate as true
        # one_item = "a", then assert(one_item) == True
        if func(one_item):
            yield one_item


# Alternative: implement this as a regular function that returns a Generator Expression
# - Generator expressions uses round parentheses "()" vs. list comprehensions uses  squares brackets "[]"
# - Generator expressions returns one element at a time vs. list comprehension returns lists that comsume more memory
def yield_filter_generator_expression(data, func):
    return (one_item for one_item in data if func(one_item))


if __name__ == "__main__":
    for item in yield_filter("abcde", my_func):
        print(item)

    print()
    for item in yield_filter_generator_expression("abcde", my_func):
        print(item)