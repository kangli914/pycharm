#!/usr/bin/env python3

"""ex49 return time and item"""

import time


'''
Normally, invoking a function multiple times means that the local variables are
reset with each invocation. 
However, a generator function works differently: it’s only
invoked once, and thus has a single stack frame. so local variables are NOT reset
'''
def elapsed_since(data):
    last_time = None
    for item in data:
        curr_time = time.perf_counter()
        delta = curr_time - (last_time or curr_time)
        last_time = time.perf_counter()
        yield (item, delta)


if __name__ == "__main__":
    for item in elapsed_since("abcde"):
        print(item)
        time.sleep(1)
