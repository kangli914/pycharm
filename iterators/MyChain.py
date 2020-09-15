
"""generator function can iterate a set of collections"""

def chain(*args):
    # print(type(args)) 
    for arg in args:
        for item in arg:
            yield item

for one_item in chain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)
