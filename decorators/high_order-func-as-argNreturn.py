"""
    exmaple of returning the fucntion as the result of other functions and pass function as argument
    this example pass external functions (add, sub) as outter functions (e.g. in this case free variables are those fucntion for closure).
    *args <-- add/supper_add/sub
    **kwargs <-- (1, 2, 3)
"""

import logging
logging.basicConfig(filename="example.log", level=logging.INFO)


def add(x, y, z):
    return x+y+z

def supper_add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def sub(x, y):
    return x-y

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

# remember when pass in function, you don't want passing function to be executed so try without ()
# at this point, we simply just created a new function called add_logger, which is equally to log_func and we haven't called or executed the new function at this monment
add_logger = function_logger(add) 

add_logger(1, 2, 3)




supperadd_logger = function_logger(supper_add)
supperadd_logger(1, 2, 3, 4, 5, 6, 7, 8, 9)
