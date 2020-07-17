class Car:
    """Simple Car object"""


    # 2 types of variables:
    # - class attribute( = class variable = static variable)
    # - instance attribute( = instance variable)
    #
    # 3 types of method:
    # - instance method (e.g. access through self)
    # - class method (use Class name and keyword and decorator @classmethod to access class variable)
    # - static method(use Class name to call and has nothing to do with class variable or static variable, decorator @staticmethod , no need self or cls)
    #
    # Use attributes(properties/data) and methods(behaviors) to define the properties and behaviors of an object
    # Class attribute/class variable/static variable: attributes that have the same value for all class instances
    made = "Made in Canada"

    # Instance attributes/instance variable: attributes created in .__init__() are called instance attributes
    def __init__(self, color, mileage):
        """initilize the car.
        
        :param str color: string of color
        :param int mileage: integer
        :returns: dic with something
        """
        self.color = color
        self.mileage = mileage

    # methods: without this __str__ calling print will return object memory address instead of string
    # <__main__.Car object at 0x7f1754d8e390>
    def __str__(self):
        return f"the {self.color} car has {self.mileage}."

if __name__ == "__main__":
    
    # A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
    # Class level doc
    print(Car.__doc__)
    print(repr(Car.__doc__))
    # Function doc
    print(Car.__init__.__doc__)
    
    # class instance magic method: __str__
    print(str(Car("blue", 20000)))
    print(str(Car("red", 40000)))
    print(Car("yellow", 60000))
    
    blue_car = Car(color="blue", mileage=20_000)
    red_car = Car(color="red", mileage=30_000)
    # ^ different object:
    # blue_car @ <__main__.Car object at 0x7f4e9620b4d0>
    # red_car <__main__.Car object at 0x7f4e96064150>
    red_car
    print(blue_car)
    print(red_car)
    if (blue_car is red_car): 
        print("same object")
    else:
        print("different object")

    # Class attribute (atrribute is shared among class instances )
    car1 = Car("black", 80000)
    car2 = Car("grey", 100000)
    print(f"black car before changing class made attribute {car1.made}")
    # black car changed the Class attribute then gry car see the change too
    car1.made = "made in China"
    print(f"grey car after changing class made attribute {car1.made}")
