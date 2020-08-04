
"""passing a function (e.g. square, cube ) as arguments"""
""" https://www.youtube.com/watch?v=kr0mpwqttM0"""

def square(x):
    return x * x

def cube(x):
    return x * x * x

# regular version
def new_container(func, list):
    """take function as arguments"""
    new_list = []
    for item in list:
        new_list.append(func(item))
    return new_list


## generator version
def new_generator(func, list, max=0):
    """a generator function"""
    
    count = 0
    for i in list:
        v = func(i)
        print(f"yeilded/to return a value: {v}")
        count +=1
        yield v

        if max and count >= max:
            break

# regular
# remember when pass in function, you don't want passing function to be executed so try without ()
new_square = new_container(square, [1, 2, 3, 4])
print(new_square)
print("\n")

## using generators
g1 = new_generator(cube, [1, 2, 3, 4, 5])
print(type(g1))
g1.__next__()
g1.__next__()
g1.__next__()
g1.__next__()
g1.__next__()
print("\n")

## using generators 
## create a list of 100 integers
my_list = [*range(1, 101)]
g2 = new_generator(cube, my_list, max=5)
for i in g2:
    print(f"returned type: {type(i)}, returned value from the g2 generator: {i}")
print("\n")


g3 = new_generator(cube, my_list, max=20)
empty_list = []

while True:
    v = next(g3)
    print(v)
    empty_list.append(v)

