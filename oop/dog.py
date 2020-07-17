class Dog:
    """Dog base class"""

    # Class attribute:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

if __name__ == "__main__":
    print(Dog("albert", 5).speak("Wof"))
    # print(Dog("albert", 5))