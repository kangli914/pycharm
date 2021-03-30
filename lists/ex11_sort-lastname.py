#!/usr/bin/env python3

"""Sort the phone book data in a list of dicts by last name then first name."""

from operator import itemgetter, attrgetter

# using ref: call sort by lambda func: https://docs.python.org/3/howto/sorting.html#sortinghowto
def sort_by_lastnames(data):
    data = sorted(data, key=lambda person: [person["last"], person["first"]])
    print_names(data)

def print_names(data):
    for idx, person in enumerate(data, 1):
        print(f"#{idx}, {person['last']}, {person['first']}")

    # for person in data:
    #     print(f"{person['last']}, {person['first']}")

def alphabetize_names(data):
    sort_by_lastnames(data)
    # print_names(data)


people = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Donald", "last": "Tod", "email": "donald@lerner.co.il"},
    {"first": "Vladimir", "last": "Petral", "email": "vladimir@lerner.co.il"}
]

alphabetize_names(people)
