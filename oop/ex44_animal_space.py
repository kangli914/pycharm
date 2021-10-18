#!/usr/bin/env python3

"""A class add animal to the cage based on its size."""

# Base class
class Animal():
    def __init__(self, color, legs) -> None:
        self.color = color
        self.legs = legs
        self.species = self.__class__.__name__

    def __repr__(self) -> str:
        return "%s %s %d" % (self.color, self.species, self.legs)


# Base class
class Cage():
    # num_animals = 1
    dimensions = 10

    def __init__(self, cage_id):
        self.animals = []
        self.cage_id = cage_id
        self.space_left = Cage.dimensions

    # we use the splat (*) operator to grab all arguments in a single tuple (animals)
    def add_animals(self, *animals_to_add):
        for animal in animals_to_add:
            # if len(self.animal.space) > Cage.dimensions:
            if (self.space_left - animal.space) < 0:
                raise ValueError(f"Sorry! Animal has exceeded the cage space: {Cage.dimensions}")
            self.animals.append(animal)
            self.space_left -= animal.space


# Added animal space instance to subclass
class SizedAnimal(Animal):
    # def __init__(self, color, legs, space):
    #     super().__init__(color, legs)
    #     self.space = space

    # rewrite init to take take all arguments in a single tuple for a init
    def __init__(self, *args):
        color, legs, space = args
        # print(color)
        # print(legs)
        # print(space)
        super().__init__(color, legs)
        self.space = space

    def __repr__(self) -> str:
        return "Animal color: %s, Animal species: %s, Animal legs: %d, Animal space: %d" \
               % (self.color, self.species, self.legs, self.space)


if __name__ == "__main__":
    sized_animals = [ SizedAnimal(*animal) for animal in (("red", 2, 4), ("white", 4, 6)) ]
    print(sized_animals)

    cage = Cage("1000")
    cage.add_animals(*sized_animals)
