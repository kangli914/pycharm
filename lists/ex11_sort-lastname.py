#!/usr/bin/env python3

"""Sort the phone book data in a list of dicts by last name then first name."""

from operator import itemgetter, attrgetter

# using ref: call sort by lambda func: https://docs.python.org/3/howto/sorting.html#sortinghowto
def sort_by_lastnames(data):
# We can do this by taking advantage of the key parameter (key=) to sorted. The value
# passed to that key parameter (key=) must be a function that takes a single argument.
# The function will be invoked once per element, and the function’s return value will be used
# to sort the values.
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
    {"first": "ceuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "bonald", "last": "Tod", "email": "donald@lerner.co.il"},
    {"first": "aladimir", "last": "Petral", "email": "vladimir@lerner.co.il"}
]

# way 1
alphabetize_names(people)

# way 2
people.sort(key=lambda x: (x['last'], x['first']), reverse=False)
print_names(people)

#sort a list:
people_list = ["a davud", "b jenny", "c tom", "d even"]
# sory by last name, first name
print(sorted(people_list, key=lambda person: (person.split()[-1].lower(), person.split()[-2].lower())))
