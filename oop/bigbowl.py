#!/usr/bin/env python3

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoop = 2

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for scoop in args:
            if len(self.scoops) >= self.max_scoop:
                raise ValueError(f"excced limit of {self.max_scoop}")
            self.scoops.append(scoop)

    def __repr__(self):
        return "\n".join([scoop.flavor for scoop in self.scoops])

class BigBowl(Bowl):
    max_scoop = 5

    def __init__(self):
        super().__init__()

if __name__== "__main__":
    big_bowl = BigBowl()
    big_bowl.add_scoops(*[Scoop(flavor) for flavor in ("apple", "pear", "cherry")])
    print(big_bowl)
