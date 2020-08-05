"""decorator version of high_order-func-as-argNreturn.py"""

import logging
logging.basicConfig(filename="example.log", level=logging.INFO)

def function_logger(out_func):

    # here out_func will be "rememberred" by the log_func even after it  finished
    # This is the concept of a closure

    # '*args' means it takes in any number of (positional) arguments to this function
    # here **kwargs doesn't do anything
    def log_func(*args, **kwargs):
        # inner function 
        logging.info(f"Running {out_func.__name__} with arguments {args}") # it prints out the arguments that we used with that functions
        print(out_func(*args))  # we are running the fucntion (e.g. out_func) that we passed in which could be ither add or sub 
    return log_func

@function_logger
def add(x, y, z):
    return x+y+z

@function_logger
def supper_add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def sub(x, y):
    return x-y





add(1, 2, 3)
supper_add(1, 2, 3, 4, 5, 6, 7, 8, 9)