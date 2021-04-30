#!/usr/bin/env python3

"""Ask user for sort option.

Define a list of tuples, in which each tuple contains the name, length (in min-utes),
and director of the movies nominated for best picture Oscar awards last year.
Ask the user whether they want to sort the list by title, length, or director’s
name, and then present the list sorted by the user’s choice of axis.
"""

MOVIES = [("Double Seven", 120, "James Bond"), ("New Change Line", 90, "David Smith"), ("X Man", 130, "Bob Green")]

while True:
    sort_idx = int(input("Sort by Title(1), Lengh(2) or Director Name:(3) or enter 4 to break: "))
    if sort_idx == 4:
        break
    for movie in sorted(MOVIES, key=lambda m: m[sort_idx - 1]):
        print("{0:15} {1:3} {2:15}".format(*movie))
