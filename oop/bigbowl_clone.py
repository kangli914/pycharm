#!/usr/bin/env python3

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoop(self, *arg):
        for scoop in arg:
            self.scoops.append(scoop)

    def __repr__(self):
        "\n".join([scoop.flavor for scoop in self.scoops])

s = Bowl()
s.add_scoop(*[Scoop(flavor) for flavor in ("apple", "strewbarry", "pineapple")])
print(s)
