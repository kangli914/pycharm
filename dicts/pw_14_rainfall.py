#!/usr/bin/env python3

from collections import defaultdict

""" print out city rainfall """


city_rainfall = dict()
city_rainfall_default = defaultdict(int)


def get_rainfall():
    """Use reguler dictionary."""
    while True:
        city = input("Enter City>: ").strip().capitalize()

        # given empty city print out all 
        if not city:
            for k, v in city_rainfall.items():
                print(f"{k}: {v} millimeters")
            break

        else:
            rain = int(input("Entry Rainfall>: "))
            city_rainfall[city] = city_rainfall.get(city, 0) + rain


def get_rainfall_default():
    """Use defaultdict dictionary from the collection."""
    while True:
        city = input("Enter City>: ").strip().capitalize()

        if not city:
            break
        else:
            rain = int(input("Entry Rainfall>: "))
            # city_rainfall_default[city] = city_rainfall_default[city] + rain
            city_rainfall_default[city] += rain

    for k, v in city_rainfall_default.items():
        print(f"{k}: {v} millimeters")


# get_rainfall()


get_rainfall_default()
