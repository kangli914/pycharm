#!/usr/bin/env python3

""" print out city rainfall """

city_rainfall = dict()


def get_rainfall():

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


get_rainfall()
