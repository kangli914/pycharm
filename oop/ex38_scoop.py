#!/usr/bin/env python3

"""A simple Scoop class represent icecream scoop."""


class Scoop:
    """Scoop class has the flavor."""

    def __init__(self, flavor):
        """Init the falvor."""
        self.flavor = flavor

    def get_flavor(self):
        """Get the flavor."""
        return self.flavor


# option 1 - create a list of Scoop object first then enumerate them
list_scoops = [Scoop("chocolate"), Scoop("vanilla"), Scoop("persimmon")]
for idx, scoop in enumerate(list_scoops, 1):
    print("#{0:1} {1:6}".format(idx, scoop.get_flavor()))


# option 2 - use list comprehension to create a list of Scoop object
for idx, scoop in enumerate([Scoop(flavor) for flavor in ("chocolate", "vanilla", "persimmon")], 1):
    print("#{0:1} | {1:6}".format(idx, scoop.flavor))
