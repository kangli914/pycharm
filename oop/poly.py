"""Plolymorphism
- Concept of dynamic methods chosen at runtime
- Subclasses must override the base classes method
- Useful for lists of different types of subclasses: 
  each sub class has a different implementation of method. so when super class method is called (e.g. call from super class object: pet.talk() ), it chooses which method to run depending on its subclasses implementation 
"""

class Pet:
    """Polymorphism example - base Pet class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # recall from car.py where w/o implementating this __str__, print(Pet) will return the memory address "<__main__.Pet object at 0x7f09f2b59510>" instead of string
    def __str__(self):
        return f"This is {self.name} from __str__()"

    #
    def talk(self):
        # return f"base class can not talk"
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Pet):
    """Polymorphism example - child Cat class"""

    def __init__(self, name, age):
        super().__init__(name, age)     # you can call super class method this way

    def __str__(self):
        return f"This is {self.name} has {self.age} old from __str__()"

    def talk(self):
        return f"Meowww from {self.name} class"


class Dog(Pet):
    """Polymorphism example - child Dog class"""
    
    def __init__(self, name, age, insurance):
        super().__init__(name, age)
        self.insurance = insurance

    def __str__(self):
        return f"This is {self.name} has {self.age} old with monthly insurance premium of {self.insurance}"

    def talk(self):
        return f"Wofff from {self.name} class"


pet = Pet("pet", 1)
cat = Cat("cat", 10)

print(pet.__doc__)
print(pet)
print(cat.__doc__)
print(cat)

print(f"is cat a cat? {isinstance(cat, Cat)}")
print(f"is cat a pet? {isinstance(cat, Pet)}")
print(f"is pet a cat? {isinstance(pet, Cat)}")
print(f"is Cat a child class of Pet class? {issubclass(Cat, Pet)}")
print(f"is Pet a child class of Cat class? {issubclass(Pet, Cat)}")


# Plolymorphism
pets = [Cat("cat2", 1), Dog("dog2", 2, 1000), Pet("pet2", 3)]
print("\n")

for pet in pets:
    print(f"object {pet.name}, has age {pet.age}, says {pet.talk()} ")