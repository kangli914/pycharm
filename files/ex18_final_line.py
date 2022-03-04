#!/usr/bin/env python3

"""Print the last line of the file."""

import os


'''
- the built-in open function can return a number of different objects, such as TextIOWrapper or BufferedReader
- These objects all implement the same API for working with files, we call them "file-like object"
- the file-like objects are all iterable so we use iterarate the elememnts

>>> f=open('/etc/passwd')
>>> print(type(f))
<class '_io.TextIOWrapper'>


# word 'with' is called context managers
'''

file = "apache.log"
#  returns current working directory of a process
path = os.getcwd()

# Open a specific file in a directory vs. open a list of files-like objects (e.g. from ex50_all_lines.py):  
# os.getcwd() vs.
# os.listdir() & os.path.job()
'''
files = [open(os.path.join(path, filename)) for filename in os.listdir(path)]
'''



# 1) read from lines
with open(f"{path}/dicts/{file}", "r") as reader:
    # print("{0:20} {1}".format( f"last line #: {len(reader.readlines())}", reader.readlines() ))
    for line in reader.readlines():
        '''
        each line already ends with a newline character. This can
        lead to doubled whitespace between printed output. The solution is to stop print
        from displaying anything by overriding the default \n value in the end parameter. By
        passing end='' , we tell print to add '' , the empty string, after printing final_line
        '''
        print(line, end="")

print()

# 2) read from file object directly - memory efficient and fast
with open(f"{path}/dicts/{file}", "r") as f:
    # loop over the file object. This is memory efficient and fast
    for line in f:
        print(line, end="")

    # read all the lines of a file in a list
    # list(f) or f.readlines()

print()

with open(f"{path}/dicts/{file}", "r") as f1:
    print(f"last line:\n {f1.readlines()[-1]}")


with open(f"{path}/dicts/{file}", "r") as f2:
    print(f"last line:\n {list(f2)[-1]}")



# code for read from binary file:
'''
when u open a nontext file, such as a PDF or a JPEG, python expects the contents of
a file to be valid UTF-8 formatted Unicode strings. Binary files, by definition, don’t use
Unicode. When Python tries to read a non-Unicode string, it’ll raise an exception, com-
plaining that it can’t define a string with such conten

'''
with open(filename, 'rb') as f:
    while True:
        # Reads up 1000 bytes and returns them as a bytes object
        one_chunk = f.read(1000)
        if not one_chunk:
            break
        print(f'This chunk contains {len(one_chunk)} bytes')