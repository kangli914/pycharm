#!/usr/bin/env python3

"""Create a dictionary using from a list using the comprehension."""

d = {word: len(word) for word in "a bc efg hijk".split()}
print(d)
