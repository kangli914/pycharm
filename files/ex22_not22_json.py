#!/usr/bin/env python3

"""
Find the users have completed the most tasks.

Read in from an endpint in a array of objects with unique user ids and determine which users
have completed (completed = true) the most tasks. The user could be one or multiple.
"""

import json
import sys

import requests


def users_completed_collections(data):
    """Find the users who finishes reading the books given a list.

    Given data is list and return a dictionary containing a list of users and the number/count of books they finished."""
    users_collections = {}
    try:
        for item in data:
            # get user id and default to None if not exists
            user_id = item.get("userId", None)
            if item.get("completed", None):
                # if user is None so it has not added to the collections yet to avoid key error
                user_id_exist = users_collections.get(user_id, None)
                if not user_id_exist:
                    users_collections[user_id] = 1
                else:
                    users_collections[user_id] += 1
    except Exception as e:
        sys.exit(f"Some thing went wrong to create the user collections: {e}!")

    return users_collections


def sort_user_collections(data):
    """Sort by highest to lowest completed count given a user dictionary collections

    Given data is a dictionary and return a sorted list of tuples.
    """

    return sorted(data.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    source = "https://jsonplaceholder.typicode.com/todos"
    res = requests.get(source)

    # to deserialization/decode: json.loads(res.text) == res.json()
    # print(type(json.loads(res.text)))
    # print(type(res.json()))
    # assert json.loads(res.text) == res.json(), "not equal"  # they are equal and type is <class 'list'>

    # get a collections where has user and counts for book completion
    users = users_completed_collections(res.json())
    # sort the list from hightest to lowest
    top_users = sort_user_collections(users)
    print(type(top_users))
    print("\n ".join( [ f"user id: {k}, completed books: {v}" for k,v in top_users] ))
    # for k,v in top_users:
    #     print(k, v)
