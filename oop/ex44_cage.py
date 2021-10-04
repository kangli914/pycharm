#!/usr/bin/env python3

"""A class where print the gage with the added animal."""

class Animal():

    def __init__(self, color, legs) -> None:
        self.color = color
        self.legs = legs
        self.species = self.__class__.__name__

    def __repr__(self) -> str:
        return "%s %s, %d" % (self.color, self.species, self.legs)


class Cage():

    def __init__(self, cage_id) -> None:
        self.animals = []
        self.cage_id = cage_id

    def add_animals(self, *animals_to_add):
        for animal in animals_to_add:
            self.animals.append(animal)

    '''
    The join() string method returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.
    
    text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

    # join elements of text with space
    print(' '.join(text))

    # Output: Python is a fun programming language
    '''

    def __repr__(self) -> str:
        new_list = [(self.cage_id, animal.color, animal.legs) for animal in self.animals]
        return " ".join(new_list)


if __name__ == "__main__":
    c1 = Cage(1)
    sheep = Animal("while", 4)
    c1.add_animals(sheep)
    c1.add_animals(Animal("bird", 2), Animal("wolf", 4))

    print(c1)


