import time


def quicker_fibonacci(func):
    """
    high order function version of fibonacci:
    if it's in cache, return cached value,
    else not in cache, then call original fib for calcs value
    """

    cached = {}

    def wrapper(n):
        if n not in cached:
            # if it's not, add it to the cache and later return the cache which was calculated from the func()
            cached[n] = func(n)
        
        return cached[n]

    return wrapper

@quicker_fibonacci
def fib(n):
    """basic fibonacci version - most inefficient"""
    if n <= 1:
        return n 
    
    else: 
        return fib(n-2) + fib(n-1)


#basic version:
# result: 102334155
# start: 1596644300.7906682 end: 1596644344.121298 Total(sec): 43.33
# start = time.time()
# print("result:", fib(40))
# stop = time.time()
# print("start:", start, "end:", stop, "Total(sec):", stop-start)
# print("\n")



# # note - key is the function name is *same as* before 'fib'
# result: 102334155
# start: 1596649210.2518868 end: 1596649210.251928 Total(sec): 4.124641418457031e-05
# start = time.time()
# fib = quicker_fibonacci(fib)
# print("result:", fib(40))
# stop = time.time()
# print("start:", start, "end:", stop, "Total(sec):", stop-start)


# @quicker_fibonacci "decorator" is equivent to 'fib = quicker_fibonacci(fib)'
start = time.time()
print("result:", fib(40))
stop = time.time()
print("start:", start, "end:", stop, "Total(sec):", stop-start)