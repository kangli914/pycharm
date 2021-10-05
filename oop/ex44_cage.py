#!/usr/bin/env python3

"""A class where print the gage with the added animal."""

class Animal():

    def __init__(self, color, legs) -> None:
        self.color = color
        self.legs = legs
        self.species = self.__class__.__name__

    def __repr__(self) -> str:
        return "%s %s %d" % (self.color, self.species, self.legs)


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
        # new_list = [(self.cage_id, animal.color, animal.legs) for animal in self.animals]
        # return " ".join(new_list)
        '''
        - take each animal in self.animals and use a generator expression (i.e., a lazy form of list comprehension) to return a sequence of strings
        - each string in that sequence will consist of a tab followed by the printed representation of the animal
        - e.g. ['\twhile Animal 4', '\tbird Animal 2', '\twolf Animal 4']
        - then feed the result of our generator expression to str.join , which puts newline characters between each animal
        '''
        output = f"Cage #{self.cage_id}\n"
        """
        output = ["\t" + str(animal) for animal in self.animals]
        print(f"output type is: f{type(output)}")
        print(output)
        output type is: f<class 'list'>
        ['\twhile Animal 4', '\tbird Animal 2', '\twolf Animal 4']
        """

        # here str(animal) automicallly calling __repr__ in Animal class
        output += "\n".join("\t" + str(animal) for animal in self.animals)
        return output
        

if __name__ == "__main__":
    c1 = Cage(1)
    sheep = Animal("while", 4)
    c1.add_animals(sheep)
    c1.add_animals(Animal("bird", 2), Animal("wolf", 4))

    c2 = Cage(2)
    c2.add_animals(*[ Animal(animal[0], animal[1]) for animal in [("cat", 4), ("dog", 4)] ])

    print(c1)
    print(c2)


