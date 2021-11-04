#!/usr/bin/env python3

"""House animals to the cage."""

from ex44_cage import Animal, Cage


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Bird(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class DangerousAssignmentError(Exception):
    pass


class HousingCage(Cage):
    '''
    my_dict = {Animal: "abc"}   # key is a class type
    b = dict(Animal="abc")      # key is a string type
    >>> for a in my_dict:
        ...     print(a)
    <class 'ex44_cage.Animal'>
    >>>     print(type(a))
    File "<stdin>", line 1
    print(type(a))
    IndentationError: unexpected indent
    >>> for a in my_dict:
        ...     print(type(a))
    <class 'type'>
    >>> for a in b:
        ...     print(type(a))
    <class 'str'>
    >>> for a in my_dict:
        ...     print(a)
    <class 'ex44_cage.Animal'>
    >>> for a in b:
        ...     print(a)
    Animal
    '''


    # class attribute
    '''
    Note: here although Wolf, Sheep, Snake, Bird as class but to access the keys, they(keys) are really string
        for key in cage_1.housing_rules.keys():
            print(type(key))
        <class 'str'>
        <class 'str'>
        <class 'str'>
        <class 'str'>
    '''
    # note, the following way results key as a string type
    # housing_rules = dict(Wolf=[Wolf, Sheep],
    #                     Sheep=[Sheep, Wolf],
    #                     Snake=[Snake, Bird],
    #                     Bird=[Snake, Bird])

    # note, the following 2 ways results key as class type than a string type
    housing_rules = dict([(Wolf, [Wolf, Sheep]),
                          (Sheep, [Wolf, Sheep]),
                          (Snake, [Snake, Bird]),
                          (Bird, [Snake, Bird]),
                        ])
    # housing_rules = {Wolf: [Wolf, Snake],
    #                  Sheep: [Wolf, Sheep],
    #                  Snake: [Snake, Bird],
    #                  Bird: [Snake, Bird]}

    def __init__(self, cage_id):
        super().__init__(cage_id)

    def add_animals(self, *animals_to_add):
        for animal in animals_to_add:
            for animal_in_stage in self.animals:
                if type(animal) not in HousingCage.housing_rules[type(animal_in_stage)]:
                    raise DangerousAssignmentError(f'You cannot put a {type(animal)} with a {type(animal_in_stage)}!')
            self.animals.append(animal)


    def __repr__(self):
        output = f"Cage {self.cage_id}\n"
        output += "\n".join("\t" + str(animal) for animal in self.animals)
        return output


if __name__ == "__main__":
    wolf = Wolf("grey")
    sheep = Sheep("white")
    bird = Bird("red")
    snake = Snake("black")

    cage_1 = HousingCage("001")
    cage_1.add_animals(wolf)
    cage_1.add_animals(sheep)
    # cage_1.add_animals(bird)

    print(cage_1)
