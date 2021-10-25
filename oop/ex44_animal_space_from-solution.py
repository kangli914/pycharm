#!/usr/bin/env python3

"""A class add animal to the cage based on its size.
provided from solutions - https://github.com/reuven/python-workout/blob/master/ch09-objects/e44b2_animal_space.py
"""

class Animal():
    def __init__(self, color, legs):
        self.spacies = self.__class__.__name__
        self.color = color
        self.legs = legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.legs} legs'


class SizedAnimal(Animal):
    space_required = 4

    def __init__(self, color, legs):
        super().__init__(color, legs)


class Cage():

    def __init__(self, cage_id, total_space):
        self.animals = []
        self.cage_id = cage_id
        self.total_space = total_space

    # sum up current animal size together
    def space_used(self):
        return sum(animal.space_required for animal in self.animals)

    def add_animals(self, *animals):
        for animal in animals:
            if self.space_used() + animal.space_required > self.total_space:
                raise ValueError(f"Sorry! Animal has exceeded the cage space: {self.total_space}")
            self.animals.append(animal)

    def __repr__(self):
        output = f"Cage #{self.cage_id}\n"
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output

if __name__ == "__main__":
    c1 = Cage(1, 10)

    c1.add_animals(SizedAnimal("white", 4))
    print(c1)

    c1.add_animals(*[SizedAnimal(animal_tuple[0], animal_tuple[1]) for animal_tuple in [("red", 4), ("blue", 4)]])
    print(c1)
