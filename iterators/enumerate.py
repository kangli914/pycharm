class Enumerate():
    """ EX #46

    https://github.com/reuven/python-workout/blob/master/ch10-iterators/e46_myenumerate.py
    
    Create your own MyEnumerate class, such that someone can use it instead of enumer-ate. 
    It will need to return a tuple with each iteration, with the first element in the
    tuple being the index (starting with 0) and the second element being the current ele-
    ment from the underlying data structure. Trying to use MyEnumerate with a noniter-
    able argument will result in an error.
    
    usage:
    for index, letter in enumerate('abc'):
        print(f'{index}: {letter}')

    another good youtube exmaple: https://www.youtube.com/watch?v=BC77x_GLmxo&list=PL1A2CSdiySGLPTXm0cTxlGYbReGqTcGRA&index=5
    """

    def __init__(self, data, index=0):
        self.data = data
        self.index = index  # instance attribute to keep track of the curren index

    def __iter__(self):
        """retrun a iterator"""

        return self

    def __next__(self):
        """__next__ implementation should either return a value or raise StopIteration"""

        while self.index < len(self.data):
            item = self.data[self.index]
            print(f"__next__() returning {item} at index {self.index}")
            self.index += 1
            return (self.index-1, item)

        print("__next__() and the end of dataset is reached and raised 'StopIteration'")
        raise StopIteration


enumerate = Enumerate('abc', index=0)
for index, letter in enumerate:
    print(f"index: {index}; letter: {letter}") 

# The hasattr() method returns true if an object has the given named attribute and false if it does no
assert hasattr(enumerate, '__iter__')