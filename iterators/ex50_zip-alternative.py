#!/usr/bin/env python3

"""Ex50 - Use generator function that reimplements zip() to iterate multi dataset in parallel."""

# ref: https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel/60842028#60842028
# You can bundle the nth elements into a tuple, then pass them out with a generator function.

# - The function takes *args as a parameter, meaning that args will be *a tuple* when
# our function executes. since it’s a tuple, we can iterate over its elements, no matter
# how many there might be
# - min() function returns item with the lowest value in an *iterable*.


def my_zip(*data_sets):
    min_length = min(len(one_set) for one_set in data_sets)
    # or using map with len() function
    # map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    #   for i in range(min(map(len,lists)))

    print(f"sets minimal length is: {min_length}")
    for i in range(min_length):
        #  bundle the nth elements into a tuple, then pass them out with a generator function
        yield tuple(one_dataset[i] for one_dataset in data_sets)


if __name__ == "__main__":
    for item in my_zip('abcd', [10, 20, 30]):
        print(item)
