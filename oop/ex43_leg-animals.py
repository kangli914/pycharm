#!/usr/bin/env python3

"""Define several new classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal, all of which inherit from Animal, 
and dictate the number of legs on each instance."""

class Animal():
    """Base class for animals. Not meant to be instantiated."""

    def __init__(self, color) -> None:
        self.color = color
        self.species = self.__class__.__name__
        # self.legs = legs

    def __repr__(self) -> str:
        # return '%s %s, %d legs' % (self.color, self.species, self.legs)
        return '%s %s' % (self.color, self.species)

class TwoLeggedAnimal(Animal):

    def __init__(self, color) -> None:
        super().__init__(color)
        self.legs = 2

    def __repr__(self) -> str:
        # return '%s %s, %d legs' % (self.color, self.species, self.legs)
        return '%s %s, %d legs' % (self.color, self.species, self.legs)

class FourLeggedAnimal(Animal):

    def __init__(self, color) -> None:
        super().__init__(color)
        self.legs = 4

    def __repr__(self) -> str:
        # return '%s %s, %d legs' % (self.color, self.species, self.legs)
        return '%s %s, %d legs' % (self.color, self.species, self.legs)

if __name__ == "__main__":
    sheep = FourLeggedAnimal("white")
    print(sheep)

    bird = TwoLeggedAnimal("red")
    print(bird)
