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

    # t1 = time.time()
    # t1 = int(round(time.time() * 1000))
    t1 = int((time.time() * 1000))
    yield
    # t2 = time.time() - t1
    # t2 = int(round(time.time() * 1000)) - t1
    t2 = int((time.time() * 1000)) - t1
    print("ran in : {} secs".format(t2))

def original_dummy_func(name, age):
    import time
    print("original_dummy function ran with arguments ({}, {})".format(name, age))
    time.sleep(0.5)


with timer_contextmanager():
    original_dummy_func("James", "30")
