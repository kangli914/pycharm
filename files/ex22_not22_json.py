#!/usr/bin/env python3

"""
Find the users have completed the most tasks.

Read in from an endpiont in a array of objects with unique user ids and determine which users
have completed (completed = true) the most tasks. The user could be one or multiple.
"""

import json
import sys
from collections import defaultdict

import requests


def users_completed_collections(data):
    """Find the users who finishes reading the books given a list.

    Given data is list and return a dictionary containing a list of users and the number/count of books they finished."""

    # option 1: use get() to avoid key erorr
    users_collections = {}

    for item in data:
        try:
            # get user id and default to None if not exists
            user_id = item.get("userId", None)
            if item.get("completed", None):
                # if user is None so it has not added to the collections yet to avoid key error
                # user_id_exist = users_collections.get(user_id, None)
                if not users_collections.get(user_id):
                    users_collections[user_id] = 1
                else:
                    users_collections[user_id] += 1
        except Exception as e:
            sys.exit(f"Some thing went wrong to create the user collections: {e}!")

    # option 2: try key error
    for item in data:
        if item["completed"]:
            try:
                user_id = item["userId"]
                # try to increment the existing user's count
                users_collections[user_id] += 1
            except KeyError:
                # This user has not been seen. Set their count to 1
                users_collections[user_id] = 1

    # option 3: use defaultdict
    users_collections = defaultdict(int)
    for item in data:
        if item["completed"]:
            user_id = item["userId"]
            users_collections[user_id] += 1

    return users_collections


def sort_user_collections(data):
    """Sort by highest to lowest completed count given a user dictionary collections

    Given data is a dictionary and return a sorted list of tuples.
    """

    return sorted(data.items(), key=lambda item: item[1], reverse=True)


def get_maximum_complete(data):
    """Given a sorted list of user and complete tuple and return the max complete in the list."""

    return data[0][1]


if __name__ == "__main__":
    source = "https://jsonplaceholder.typicode.com/todos"
    res = requests.get(source)

    # to deserialization/decode string into Python dictonary: json.loads(res.text) == res.json()
    print(type(json.loads(res.text)))
    print(type(res.json()))
    assert json.loads(res.text) == res.json(), "not equal"                # they are equal and type is <class 'list'>

    # get a collections where has user and counts for book completion
    users = users_completed_collections(res.json())
    # sort the list from hightest to lowest
    sorted_users = sort_user_collections(users)

    # sorted_users is a list
    # print(type(sorted_users))

    # sorted_users is a list of tuple: join() same as for-loop to iterate the elements
    # for (k, v) in sorted_users:
    #     print(k, v)
    print(f"users list sorted by top to bottom:")
    print("\n".join([f"user id: {k}, completed books: {v}"
                    for k, v in sorted_users]))

    max_count = get_maximum_complete(sorted_users)

    # create a list of all users who have completed the maximum number of books
    max_users_list = []
    for user_id, num_complete in sorted_users:
        if num_complete == max_count:
            max_users_list.append((user_id, num_complete))

    print()

    # https://stackoverflow.com/questions/497765/python-string-joinlist-on-object-array-rather-than-string-array
    # https://www.geeksforgeeks.org/python-list-comprehensions-vs-generator-expressions/#:~:text=So%20what's%20the%20difference%20between,memory%20efficient%20than%20the%20lists.
    '''
    So what’s the difference between Generator Expressions and List Comprehensions?
    The generator yields one item at a time and generates item only when in demand. Whereas, in a list comprehension, Python reserves memory for the whole list. Thus we can say that the generator expressions are memory efficient than the lists.
    '''
    list_comprehension = " and ".join([str(item[0]) for item in max_users_list])        # list comprehension
    generator_expression = " and ".join(str(item[0]) for item in max_users_list)        # generator expression

    print(list_comprehension)
    print(generator_expression)

    print()
    # one statement if and else
    s = "s" if len(max_users_list) > 1 else ""

    print(f"user{s} {list_comprehension} completed {max_count} books!")
