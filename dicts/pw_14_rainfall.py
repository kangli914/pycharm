#!/usr/bin/env python3

"""A rainfall programe to track rainfall."""

from collections import defaultdict


def get_rainfall():
    city_rain = defaultdict(int)

    while True:
        city = input("Enter city: ").strip()
        if not city:
            break
        try:
            rain = int(input("Amount: ").strip())
        except ValueError:
            print("Amount entered is not an integer!")
            # continue
        else:
            city_rain[city] += rain

    for k, v in city_rain.items():
        print(f"city: {k}, amount: {v}")


if __name__ == "__main__":
    get_rainfall()
