#!/usr/bin/env python3

class Animal():

    def __init__(self, color, legs):
        self.color = color
        self.species = self.__class__.__name__
        self.legs = legs

    def __repr__(self):
        print('%s %s, %d legs' % (self.color, self.species, self.legs))

class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color, 4)

s = Sheep("white")
print(s)
