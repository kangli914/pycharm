#!/usr/bin/env python3

"""A class where inheraite Cage class with a limit on animals."""

from ex44_cage import Animal, Cage


class BigCage(Cage):
    num_animals = 3  # class attribute

    def __init__(self, cage_id):
        super().__init__(cage_id)

    def add_animals(self, *animals_to_add):
        # for animal in animals_to_add:
        #     if len(self.animals) < BigCage.num_animals:
        #         self.animals.append(animal)
        #     else:
        #         print(f"exceeded the limit {BigCage.num_animals}")
        #         break
        for animal in animals_to_add:
            if len(self.animals) >= BigCage.num_animals:
                raise ValueError(f"sorry! excceeded max cage of class attribute {BigCage.num_animals}")
            self.animals.append(animal)

if __name__ == "__main__":
    c1 = BigCage(1)
    sheep = Animal("while", 4)
    c1.add_animals(sheep)
    c1.add_animals(Animal("bird", 2), Animal("wolf", 4), Animal("cat", 4))

    print(c1)
