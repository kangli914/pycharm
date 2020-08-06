"""general logger and timer decorators - https://www.youtube.com/watch?v=FsAPt_9Bf3U """

from functools import wraps                   # to preserve the information of the original function whenever we use the decorators


def logger_decorator(orig_func):
    """a decorator: logger decorator for any function"""
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
       
        # run the original function and return the result
        return orig_func(*args, **kwargs)
        # orig_func(*args, **kwargs)          # seems there is  no difference with return `orig_func` as previous line. it does not seem make a difference?
    return wrapper


def timer_decorator(orig_func):
    """a decorator: timer decorator for any function"""
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in : {} secs".format(orig_func.__name__, t2))
        # returning the result of the original function
        return result

    return wrapper

@logger_decorator               # ~=    original_dummy_func = logger_decorator(original_dummy_func)
@timer_decorator                # ~=    original_dummy_func = timer_decorator(original_dummy_func)  
def original_dummy_func(name, age):
    print("original_dummy function ran with arguments ({}, {})".format(name, age))


original_dummy_func("James", "30")
original_dummy_func("Jenny", "25")