#!/usr/bin/env python3

"""ex49 return time and item"""

import time

MINIMUM = 2

'''
Normally, invoking a function multiple times means that the local variables are
reset with each invocation. 
However, a generator function works differently: it’s only
invoked once, and thus has a single stack frame. so local variables are NOT reset
like last_time (it remember last value)
'''
def elapsed_since(data, MINIMUM):
    last_time = None
    for item in data:
        curr_time = time.perf_counter()
        delta = curr_time - (last_time or curr_time)
        
        if delta <= MINIMUM:
            time.sleep(MINIMUM - delta)

        last_time = time.perf_counter()
        yield (item, delta)


if __name__ == "__main__":
    for item in elapsed_since("abcde", MINIMUM):
        print(item)
        time.sleep(1)
