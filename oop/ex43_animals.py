#!/usr/bin/env python3

class Animal():

    def __init__(self, color, legs):
        self.color = color
        self.species = self.__class__.__name__
        self.legs = legs

    def __repr__(self):
        return '%s %s, %d legs' % (self.color, self.species, self.legs)
        

class Sheep(Animal):
    """Class for creating 4-legged sheep of any color"""

    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    """Class for creating 0-legged snakes of any color"""

    def __init__(self, color):
        super().__init__(color, 0)

s = Sheep("white")
print(s)

s = Snake("black")
print(s)