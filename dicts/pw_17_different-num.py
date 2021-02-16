#!/usr/bin/env python3

"""A function takes a single list of integers and returns the number of different integers it contains."""

def how_many_different_numbers(data):

    print(set(data))
    print(len(set(data)))



numbers = [1, 2, 3, 1, 2, 3, 4, 1]
how_many_different_numbers(numbers)
