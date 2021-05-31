#!/usr/bin/env python3

"""Beverage class with name and temperatures."""


class Beverage:
    """Beverage class."""

    def __init__(self, name, temperatures=75):
        """Initilize the name."""
        self.name = name
        self.temperatures = temperatures


# without unpacking
for i in [Beverage(item[0], item[1]) for item in (("coke", 30), ("water"), ("icec-coffee"))]:
    print(i.name, i.temperatures)


# tuple unpacking
for idx, thing in enumerate([Beverage(*item) for item in (("coke", 30), ("water", 50), ("icec-coffee",))], 1):
    print("#{0} {1:11} {2}".format(idx, thing.name, thing.temperatures))


print("*****************")
for item in (("coke", 30), ("water", 50), ("icec-coffee",)):
    print(*item)
