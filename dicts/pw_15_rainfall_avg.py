#!/usr/bin/env python3

"""Dictionary exercise 15.

This module prints the total rainfall and the average rainfall for reported days for a given city.
"""

from collections import defaultdict

database = defaultdict(list)
# database = dict()

while True:

    city = input("Entry city: ").strip()
    if not city:
        break

    rain = int(input("Entry rain fall amount: ").strip())
    database[city].append(rain)

for k, v in database.items():
    print(f"city: {k}, total rainfall: {sum(v)}, average rainfall: {sum(v)/len(v)}")
