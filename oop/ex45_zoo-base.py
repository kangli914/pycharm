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
        output = "Cage %s\n" % self.id
        output += "\n".join(f"\t\t{animal}" for animal in self.animals_cage)
        return output


class NoColorsPassedError(Exception):
    pass


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for cage in args:
            self.cages.append(cage)

    # Given a zoo z, we should be able to print all of the cages with their id numbers
    # and the animals inside simply by invoking print(zoo)
    def __repr__(self) -> str:
        output = "Zoom has cages:\n"
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

    # It takes any number of colors. Animals having any of the listed colors should be returned.
    # The method should raise an exception if no colors are passed.
    def animals_by_any_colors(self, *colors):
        if not colors:
            raise NoColorsPassedError
        return [animal for cage in self.cages
                for animal in cage.animals_cage if animal.color in colors]

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
    def total_animals_legs(self) -> int:
        # total_legs = 0
        # for cage in self.cages:
        #     for animal in cage.animals_cage:
        #         total_legs += animal.legs
        # return total_legs

        # take advantage of the built-in sum method, handing it the generator expression that goes through
        # each cage and retrieves the number of legs on each animal. The method will thus return an integer.
        return sum(animal.legs for cage in self.cages
                   for animal in cage.animals_cage)

    # Transfer animal from one Zoo to another Zoo.
    # The first animal of the specified type is removed from the zoo on which we’ve called the method and
    # inserted into the first cage in the target zoo.
    def transfer_animal(self, target_zoo, animal_to_transfer):
        # remove the animal from current Zoo
        [cage.animals_cage.remove(animal_to_transfer) for cage in self.cages
            for animal in cage.animals_cage if animal is animal_to_transfer]
        # add the animal to target Zoo
        target_zoo.cages[0].add_animals(animal_to_transfer)

    # Use kwargs to get names and values. The only valid names would be color and legs.
    # The method would then use one or both of these keywords to assemble a query that
    # returns those animals that match the passed criteria.
    def get_animals(self, **kwargs):
        print()
        # if 'color' in kwargs:
        #     # for one_color in kwargs.values():
        #     print(self.animals_by_color(one_color))
        # if 'legs' in kwargs:
        #     # for one_leg in kwargs.values():
        #     print(self.animals_by_legs(one_leg))

        print(f'{kwargs=}')
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if (('color' in kwargs and one_animal.color == kwargs['color']) or
                    ('legs' in kwargs and one_animal.number_of_legs == kwargs['legs']))]


if __name__ == "__main__":
    bird = Bird("red")
    wolf = Wolf("grey")
    snake = Snake("black")
    cat = Cat("grey")
    # print(bird)

    cage_1 = Cage("001")
    cage_2 = Cage("002")
    # add bird to cage_1 which will be transferred/removed later from current Zoo
    cage_1.add_animals(bird, wolf)
    cage_2.add_animals(snake, cat)
    # print(cage_1)

    zoo_1 = Zoo()
    zoo_1.add_cages(cage_1, cage_2)
    print(zoo_1)
    zoo_2 = Zoo()
    zoo_2.add_cages(Cage("003"))
    print()

    # print(zoo.animals_by_color("grey"))
    print(zoo_1.animals_by_legs(0))
    print(f"Total legs: {zoo_1.total_animals_legs()}")
    print()

    print(f"Animals by colors:\n\t {zoo_1.animals_by_any_colors('grey', 'red', 'black')}")
    # print(f"Animals by colors:\n\t {zoo_1.animals_by_any_colors()}")
    print()

    zoo_1.transfer_animal(zoo_2, bird)
    print("Transferred the animal bird from zoo1 to zoo2:")
    print(zoo_2)
    print(zoo_1)

    print(zoo_1.get_animals(color="red", legs=4))

