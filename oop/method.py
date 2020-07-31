class Person:
    """use to demostrate the differences of instance method, class method and static method
    # 3 types of method: (method e.g. set behaviors)
    # - instance method (e.g. access through self through creating a object)
    # - class method (use Class name and keyword and decorator @classmethod to access class variable).
    #   Use the @classmethod as a Factory to create objects from otherwise unacceptable parameters: you should choose @classmethod over @staticmethod when you are
    #   creating an additional constructor. If what you want is a Factory method that is aware of the class that called it, then @classmethod is what you need.
    # - static method(use Class name to call and has nothing to do with class variable or static variable, decorator @staticmethod , no need self or cls)
    # ref:
    # - https://www.youtube.com/watch?v=lVfGQOzzRCM
    # - https://www.youtube.com/watch?v=pUGyU-hxw5E&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=2
    # - when to use class vs static method:
    # - https://www.programiz.com/python-programming/methods/built-in/classmethod
    # - https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner (good)
    """

    # class variable
    count = 0                       # class variable shared by all instances need to be initialized

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # instance method
    def get_name(self):
        return f"{self.first} {self.last}"

    # class method
    @classmethod
    def headcount(cls):
        cls.count += 1
        return cls.count

    # static mehtod
    @staticmethod
    def print_info():
        print(f"this class is is dummy")


p1 = Person("david", "smith")
print(p1.get_name())
print(Person.headcount())

p1 = Person("jenny", "johnson")
print(p1.get_name())
print(Person.headcount())

Person.print_info()