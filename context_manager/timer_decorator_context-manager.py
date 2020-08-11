"""
    this code is to implement the timer_decorator in decorator.py in context manager
    it fits Context Manager concepts well to make a cleaner code:
    - DO something at startup (Record start time)
    - Perform some work (unspecific work and will be different from time to time)
    - Do something at end (Report elapsed time)
"""

from contextlib import contextmanager

@contextmanager
def timer_contextmanager():
    """a context manager function: timer decorator for any function"""
    import time

    t1 = time.time()
    yield
    t2 = time.time() - t1
    print("ran in : {} secs".format(t2))

def original_dummy_func(name, age):
    print("original_dummy function ran with arguments ({}, {})".format(name, age))


with timer_contextmanager():
    original_dummy_func("James", "30")
