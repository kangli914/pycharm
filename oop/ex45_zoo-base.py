#!/usr/bin/env python3

""" A Zoo class contain cage objects, and they in turn will contain animals.
"""


class Animal:
    """ Base class."""
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
        self.species = self.__class__.__name__

    def __repr__(self) -> str:
        return "Animal %s with %s color has %d legs" % \
               (self.species, self.color, self.legs)


class Bird(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Cat(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Cage:
    def __init__(self, id):
        self.id = id
        self.animals_cage = []

    def add_animals(self, *args):
        for animal in args:
            self.animals_cage.append(animal)

    def __repr__(self) -> str:
        output = f"Cage {self.id}\n"
        output += "\n".join(f"\t\t{animal}" for animal in self.animals_cage)
        return output


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for cage in args:
            self.cages.append(cage)

    # Given a zoo z, we should be able to print all of the cages with their id numbers
    # and the animals inside simply by invoking print(zoo)
    def __repr__(self) -> str:
        output = f"Zoom has cages:\n"
        # str.join with a generator expression here, which is slightly more efficient than
        # a list comprehension
        output += "\n".join(f"\t{str(cage)}" for cage in self.cages)
        return output

    # Get the animals with a particular color. The result should be a list of Animal objects
    def animals_by_color(self, color):
        # nested for-loop implementations
        # for cage in self.cages:
        #     print(f"In the cage with id <{cage.id}> has the following animals matching the color <{color}>:")
        #     for animal in cage.animals_cage:
        #         if animal.color == color:
        #             print(animal.species)
        # a better way: use a nested list comprehension than nested for-loop implementations
        return [animal for cage in self.cages
                for animal in cage.animals_cage if animal.color == color]

    # Get the animals with a particular number of legs. The result should be a list of Animal objects
    def animals_by_legs(self, legs):
        # for cage in self.cages:
        #     print(f"In the cage with id <{cage.id}> has the following animals having <{legs}> legs:")
        #     for animal in cage.animals_cage:
        #         if animal.legs == legs:
        #             print(animal.species)
        return [animal for cage in self.cages
                for animal in cage.animals_cage if animal.legs == legs]

    # Get the total number of legs for all animals in the zoo
    def total_animals_legs(self):
        # total_legs = 0
        # for cage in self.cages:
        #     for animal in cage.animals_cage:
        #         total_legs += animal.legs
        # return total_legs

        # take advantage of the built-in sum method, handing it the generator expression that goes through
        # each cage and retrieves the number of legs on each animal. The method will thus return an integer.
        return sum(animal.legs for cage in self.cages
                   for animal in cage.animals_cage)


if __name__ == "__main__":
    bird = Bird("red")
    wolf = Wolf("grey")
    snake = Snake("black")
    cat = Cat("grey")
    # print(bird)

    cage_1 = Cage("001")
    cage_2 = Cage("002")
    cage_1.add_animals(bird, wolf)
    cage_2.add_animals(snake, cat)
    # print(cage_1)

    zoo = Zoo()
    zoo.add_cages(cage_1, cage_2)
    print(zoo)
    print()

    print(zoo.animals_by_color("grey"))
    print(zoo.animals_by_legs(0))
    print(f"Total legs: {zoo.total_animals_legs()}")
