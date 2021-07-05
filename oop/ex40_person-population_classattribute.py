#!/usr/bin/env python3

"""Person class with class attribute population where every time creating Person it will increase Person.population."""

class Person():
    """Person has class attribue."""

    # a class attribute
    population = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.population += 1


if __name__ == "__main__":
    """Define a Person class, and a population class attribute that increases each time
    you create a new instance of Person . Double-check that after you’ve created five
    instances, named p1 through p5 , Person.population and p1.population are
    both equal to 5."""

    [Person(person_name.split()[0], person_name.split()[1]) for person_name in ("David Smith", "Jennifer Green")]
    p3 = Person(*"Larry Lee".split())

    assert p3.population == Person.population
    print(p3.population)
    print(Person.population)
