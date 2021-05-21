#!/usr/bin/env python3

"""Beverage class with name and temperatures."""


class Beverage:
    """Beverage class."""

    def __init__(self, name, temperatures=75):
        """Initilize the name."""
        self.name = name
        self.temperatures = temperatures


for i in [Beverage(item[0],item[1]) for item in (("coke", 30), ("water"), ("icec-coffee"))]:
    print(i.name, i.temperatures)