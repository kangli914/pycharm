#!/usr/bin/env python3

"""Use leg as class attributes instead of instance variable so no need to write __init__ in every subclass.

It compares to ex43_instance-leg-animals.py. here it direcly inheriated from ANimal class"""

from ex43_animals import Animal

class Sheep(Animal):

    # class attribute
    num_legs = 4

class Bird(Animal):

    # class attribute
    num_legs = 2


if __name__ == "__main__":
    sheep = Sheep("white", Sheep.num_legs)
    print(sheep)

    bird = Bird("red", Bird.num_legs)
    print(bird)
