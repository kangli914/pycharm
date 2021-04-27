#!/usr/bin/env python3

"""Read from a list of tuples and turning them into formatted output for the user"""

PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

# print(sorted(PEOPLE, key=lambda person: person[1]))
PEOPLE_SORT_LNAME = sorted(PEOPLE, key=lambda person: person[1])

for idx, (fname, lname, time) in enumerate(PEOPLE_SORT_LNAME, 0):
    print(f"#{idx}, {lname}, {fname}, {time}")