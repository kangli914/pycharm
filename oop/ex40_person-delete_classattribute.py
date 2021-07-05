#!/usr/bin/env python3

""" implement __del__ to delete a object reduce class attribute count."""

class Person():
    """sinple person class."""

    # a class attribute
    count = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        Person.count += 1

    # __del__ executes when the reference count to an object is zero
    def __del__(self):
        Person.count -= 1


if __name__ == "__main__":

    # here it will cause reference count always be zero after creating the person
    [Person(person_name.split()[0], person_name.split()[1]) for person_name in ("David Smith", "Jennifer Green")]

    p1 = Person(*"David Smith".split())
    p2 = Person(*"Jennifer Green".split())
    p3 = Person(*"Larry Lee".split())
    print(Person.count)

    del p3
    print(Person.count)