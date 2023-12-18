#!/usr/bin/env python3

"""From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell."""


import os
from pathlib import Path
# from collections import defaultdict


def open_file_safely(file, file_mode="r"):
    """Open file safely."""
    try:
        return open(file, mode=file_mode)
    except OSError:
        os.error("Erorr in open {file}")


def shell_dict(file):
    """Read from a file and return a dict to dict"""

    '''
    collections = defaultdict(dict)
    The argument passed to defaultdict() specifies the default value that will be returned. In this case, dict() is passed as the default value, which means that a new dictionary will be created as the default value for any non-existing key
    >>> default_dict['key1']
    {}
    >>> d['key1']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'key1'
    '''

    '''
    defaultdict(dict) is good for dictionary of dictionary:
    dict() is a built-in Python data type that represents a collection of key-value pairs, where each key maps to a unique value. The keys in a dictionary must be unique, immutable, and hashable, while the values can be of any type. Dictionaries are unordered, meaning that the order in which the items are stored is not guaranteed.

    On the other hand, defaultdict(dict) is a subclass of dict in the collections module that provides a default value for non-existent keys. When a non-existent key is accessed, instead of raising a KeyError, a new key-value pair is automatically created with the *default value specified, which is a new empty dict* in this case.

    Here is an example:
    >>> normal_dict = dict()
    >>> normal_dict['a'] = 1
    >>> print(normal_dict['a']) # Output: 1
    >>> print(normal_dict['b']) # Raises KeyError

    >>> from collections import defaultdict
    >>> dd = defaultdict(dict)
    >>> dd['a']['x'] = 1
    >>> print(dd['a']['x']) # Output: 1
    >>> print(dd['b']) # Output: {}
    As you can see, when a non-existent key b is accessed in the normal_dict, it raises a KeyError. Whereas, in the defaultdict(dict), a new empty dict is automatically created for the non-existent key b.

    In summary, the difference between dict() and defaultdict(dict) is that dict() does not provide a default value for non-existent keys, while defaultdict(dict) does by creating a new empty dict.

    >>> from collections import defaultdict
    >>> dd = defaultdict(dict)
    >>> dd['a']
    {}
    >>> type(dd['a'])
    <class 'dict'>
    >>> 
    >>> 
    >>> dd['a']['x'] = 1
    >>> type(dd['a'])
    <class 'dict'>
    >>> type(dd['a']['x'])
    <class 'int'>
    >>> dd
    defaultdict(<class 'dict'>, {'a': {'x': 1}})
    >>> dd['b']
    {}
    >>> dd
    defaultdict(<class 'dict'>, {'a': {'x': 1}, 'b': {}})
    '''



    # collections = defaultdict(dict)
    collections = dict()
    with open_file_safely(file) as f:
        for line in f:
            if not line.startswith(("#", "\n")):
                username, second, userid, *rest, homedir = line.strip().split(":")
                collections[username] = {username, userid, homedir}
    return collections


if __name__ == "__main__":
    dir = Path("/etc/")
    file_path = dir / "passwd"
    for k, v in shell_dict(file_path).items():
        print(k, v)
