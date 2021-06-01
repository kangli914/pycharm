#!/usr/bin/env python3

"""Simple composition where Bowl class contains a list of Scoops class."""

# from ex38_scoop import Scoop


class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    """Bowl class contains a list of Scoops classes."""

    def __init__(self):
        """Initialize scoops with empty list."""
        self.scoops = []

    # splat operator (*) means be a __!!tuple!!__ containing all of the arguments that were passed to add_scoops
    def add_scoops(self, *args):
        for scoop in args:
            self.scoops.append(scoop)

    def __repr__(self):
        """Overwrite repr return scoop string."""
        # return '\n'.join(scoop.flavor for scoop in self.scoops)
        
        flavors = None
        for scoop in self.scoops:
            flavors += scoop.flavor
        return flavors

# for idx, scoop in enumerate([Scoop(flavor) for flavor in ("chocolate", "vanilla", "persimmon")], 1):
#     print("#{0:1} | {1:6}".format(idx, scoop.flavor))

bowl = Bowl()

bowl.add_scoops([Scoop(flavor) for flavor in ("chocolate", "vanilla", "persimmon")])
bowl.add_scoops(Scoop("strewberry"))

print(bowl)
