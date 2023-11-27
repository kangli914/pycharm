#!/usr/bin/env python3

"""A rainfall programe to track rainfall."""

from collections import defaultdict

"""
Python exception:
1. Code that might raise an exception is placed in the try block.
2. If an exception occurs, the code inside the corresponding except block is executed.
3. You can have multiple except blocks to handle different types of exceptions.
4. The else block is optional and contains code that is executed if no exceptions are raised.
5. The finally block is also optional and contains cleanup code that is always executed, whether an exception occurred or not.
"""

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
