# 'dog' is python file named dog.py and 'Dog' is the class name
from dog import Dog

class GoldenDog(Dog):
    """
    Create a GoldenRetriever class that inherits from the Dog class. 
    Give the sound argument of GoldenRetriever.speak() a default value of "Bark".
    """

    def speak(self, sound="Bark"):
        #return f"{self.name} sounds {sound}"
        return super().speak(sound)

if __name__ == "__main__":
    print(Dog.__doc__)
    print(GoldenDog.__doc__)
    
    dog_base = Dog("base", 10)
    dog_child = GoldenDog("child", 1)
    
    print(dog_base.speak("wof"))


    # https://rszalski.github.io/magicmethods/#numeric
    # built in functions isinstance() and issubclass()behaves by defining magic methods:
    # __instancecheck__(self, instance)
    # __subclasscheck__(self, subclass)
    # check instnace
    if isinstance(dog_child, Dog):
        print(dog_child.speak())
    if GoldenDog.__instancecheck__(dog_child):
        print(dog_child.speak())

    # check subclass
    if issubclass(GoldenDog, Dog):
        print(dog_child.speak())
    if Dog.__subclasscheck__(GoldenDog):
        print(dog_child.speak())


    print(dog_child.__getattribute__("name"))