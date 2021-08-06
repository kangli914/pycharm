#!/usr/bin/env python3

"""A bigger bowl to inherite the base class."""

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 2

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for scoop in args:
            # if len(self.scoops) >= Bowl.max_scoops:  ### important difference (Bowl.max_scoops vs self.max_scoops) for inheritance to work!!!!! ###
            if len(self.scoops) >= self.max_scoops:
                raise ValueError(f"sorry! excceed max scoop of class attribute {self.max_scoops}")    
            self.scoops.append(scoop)

    def __repr__(self):
        # The join() method takes iterable – objects capable of returning its members one at a time. Some examples are List, Tuple, String, Dictionary and Set
        # Creates a string via str.join and a generator expression
        return "\n".join(scoop.flavor for scoop in self.scoops)

class BigBowl(Bowl):
     max_scoops = 5

     def __init(self):
         super().__init__()


if __name__ == "__main__":
    # bowl = Bowl()
    # bowl.add_scoops(*[Scoop(flavor) for flavor in ("cherry", "banana")])
    # print(bowl)
    # bowl.add_scoops(Scoop("apple"))
    # print(bowl)

    bigbowl = BigBowl()

    # https://stackoverflow.com/questions/57814195/what-does-for-x-y-in-list-mean-in-python
    # a combination of tuple/list unpacking and *args iterable unpacking. Each iterable is getting unpacked on each iteration of the for loop.

    bigbowl.add_scoops(*[Scoop(flavor) for flavor in ("cherry", "banana")])
    # bigbowl.add_scoops(Scoop("apple"))
    print(bigbowl)