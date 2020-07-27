class DatasetIterator():
    """ a simple iterator can be used in for-loop to iterator any iterable"""

    def __init__(self, data, index=0):
        self.index = index
        self.data = data
        print(f"in __init__ and initilize the index to be {self.index}")

    def __iter__(self):
        """retrun a iterator"""

        print(f"in __iter__")
        return self

    def __next__(self):
        """__next__ implementation should either return a value or raise StopIteration"""

        # built-in function next() and an iterator’s __next__() method to signal that there are no further items produced by the iterator.
        # __next__() signals that there are no further items produced by the iterator.
        if self.index >= len(self.data):
            print(f"in __next__ and the end of dataset is reached and raised 'StopIteration'")
            raise StopIteration

        item = self.data[self.index]
        self.index += 1
        print(f"in __next__ and current returning item at {self.index} with item {item} to the caller")
        return item

# for i in "abc":
#     print(i)

for item in DatasetIterator("abcd"):
    print(f"this is current item from the dataset from iterator: {item}\n")

for item in DatasetIterator("abcd", index=1):
    print(f"this is current item from the dataset from iterator: {item}\n")


'''
### executed directly: ###
in __init__ and initilize the index to be 0
in__iter__                                                                                                                                                                                                               
in __next__ and current returning item at 1 with item a to the caller 
this is current item from the dataset from iterator: a 

in __next__ and current returning item at 2 with item b to the caller 
this is current item from the dataset from iterator: b 

in __next__ and current returning item at 3 with item c to the caller 
this is current item from the dataset from iterator: c 

in __next__ and current returning item at 4 with item d to the caller 
this is current item from the dataset from iterator: d

in __next__ and the end of dataset is reached and raised 'StopIteration'


### executed from python iterative windows by *manually* calling next/interator: ###

(.venv37) perfeng:~/repo/personal/pycharm ^master $ python
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from iterators.forloop import DatasetIterator as IT
>>>
>>> dir(IT)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>>
>>>
>>>
>>> a=IT("123")
in __init__ and initilize the index to be 0
>>> next(a)
in __next__ and current returning item at 1 with item 1 to the caller
'1'
>>> next(a)
in __next__ and current returning item at 2 with item 2 to the caller
'2'
>>> next(a)
in __next__ and current returning item at 3 with item 3 to the caller
'3'
>>> next(a)
in __next__ and the end of dataset is reached and raised 'StopIteration'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/perfeng/repo/personal/pycharm/iterators/forloop.py", line 21, in __next__
    raise StopIteration
StopIteration


### calling __iter__()/iter() and __next__()/next() from python iterative windows ###

# __iter__() vs. iter() (e.g. buit-in function)
>>>
>>> a = IT("abc", 0)
in __init__ and initilize the index to be 0
>>>
>>> print(a.__iter__())
in __iter__
<iterators.forloop.DatasetIterator object at 0x7f60a411b8d0>
>>> 
>>> 
>>> print(iter(a))
in __iter__
<iterators.forloop.DatasetIterator object at 0x7f60a411b8d0>


# __next__() vs. next()
>>> 
>>> a = IT("abcd", 0)
>>>
in __init__ and initilize the index to be 0
>>> print(a.__next__())
in __next__ and current returning item at 1 with item a to the caller
a
>>> print(next(a))
in __next__ and current returning item at 2 with item b to the caller
b
>>>
>>> print(type(next(a)))
in __next__ and current returning item at 3 with item c to the caller
<class 'str'>
>>> print(type(a.__next__()))
in __next__ and current returning item at 4 with item d to the caller
<class 'str'>
>>>
>>> print(type(a.__next__()))
in __next__ and the end of dataset is reached and raised 'StopIteration'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/perfeng/repo/personal/pycharm/iterators/forloop.py", line 21, in __next__
    print(f"in __next__ and the end of dataset is reached and raised 'StopIteration'")
StopIteration
'''