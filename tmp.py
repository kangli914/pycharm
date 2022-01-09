#!/usr/bin/env python3
import os
from itertools import zip_longest

'''
def all_lines(path):
    # print(path)

    for file_idx, one_file in enumerate(os.listdir(path)):
        file = os.path.join(path, one_file)
        try:
            if file.endswith(".csv"):
                # for line in open(file):
                for line_idx, line in enumerate(open(file)):
                    yield (file, file_idx, line_idx, line)
        except OSError:
            pass


if __name__ == "__main__":
    for one_line in all_lines("iterators"):
        print(one_line)
'''

def all_files(path):
    # return the files as <class 'generator'> with "()" instead of list
    files = (os.path.join(path, f) for f in os.listdir(path) if f.endswith(".csv"))
    return files

def open_file_safely(file):
    try:
        return open(file)
    except OSError:
        return None

def alternative_lines(files):
    all_files = [open_file_safely(file) for file in files]

    # while all_files:
    #     for one_file in all_files:
    #         if one_file is None:
    #             all_files.remove(one_file)
    #             continue
    #
    #         one_line = one_file.readline()
    #
    #         if one_line:
    #             yield one_line
    #         else:
    #             all_files.remove(one_file)

    '''    
    for line in zip_longest(open(files).readline()):
        print(f"item before yield: {line}")
        yield line
    '''

    print(*all_files)
    for tuple_line in zip_longest(*all_files):
        for item in tuple_line:
            if item:
                print(item, end="")




        # print(tuple_line)
        # a, b, c = tuple_line
        # if a:
        #     print(a)
        # if b:
        #     print(b)
        # if c:
        #     print(c)


if __name__ == "__main__":
    print(type(all_files("iterators")))
    print('\n'.join(all_files("iterators")))
    print()

    files = all_files("iterators")
    alternative_lines(files)

    # for line in alternative_lines(files):
    #     print(line)
