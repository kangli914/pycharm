#!/usr/bin/env python3

"""A bowl class has class attribute to put scoop in limit for all bowls by capping the number of
scoops in a bowl at three"""

from ex38_scoop import Scoop

'''
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
'''


class Bowl():
    """A simple Bowl class contains a list of Scoops classses."""

    # class attribue serving like constant as Python doesn’t have constants, but we can simulate them with class attributes.
    max_scoops = 2

    def __init__(self):
        """Initialize scoops with empty list."""
        self.scoops = []

    def add_scoops(self, *args):
        """Add scoops to the bowl with max limit."""
        for scoop in args:
            # note access the class attribute using Class Bowl instead of objects 
            # if len(self.scoops) < Bowl.max_scoops:
            #     self.scoops.append(scoop)
            # else:
            #     raise ValueError(f"sorry! excceeded max scoop of class attribute {Bowl.max_scoops}")
            if len(self.scoops) >= Bowl.max_scoops:
                #raise Exception("Too many elements")
                raise ValueError(f"sorry! excceeded max scoop of class attribute {Bowl.max_scoops}")
            self.scoops.append(scoop)

    def __repr__(self):
        """Overwrite the printout to list the scoop object."""
        return "\n".join(scoop.flavor for scoop in self.scoops)


bowl = Bowl()
bowl.add_scoops(*[Scoop(flavor) for flavor in ("cherry", "banana")])
# print(bowl)

bowl.add_scoops(Scoop("apple"))
print(bowl)