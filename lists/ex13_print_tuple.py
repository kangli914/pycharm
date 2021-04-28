#!/usr/bin/env python3

"""Read from a list of tuples and turning them into formatted output for the user"""

from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

# print(sorted(PEOPLE, key=lambda person: person[1]))
PEOPLE_SORT_LNAME = sorted(PEOPLE, key=lambda person: person[1])

for idx, (fname, lname, time) in enumerate(PEOPLE_SORT_LNAME, 0):
    print(f"#{idx}, {lname}, {fname}, {time}")


def format_name_string(list_of_tuple):
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(list_of_tuple, key=itemgetter(1, 0)):
        print(template.format(*person))


format_name_string(PEOPLE)
