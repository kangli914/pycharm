#!/usr/bin/env python3

from ex43_animals import Animal

class SoundAnimals(Animal):

    def __init__(self, color, legs, sound):
        super().__init__(color, legs)
        self.sound = sound
    
    def __repr__(self):
        return '%s -- %s %s, %d legs' % (self.sound, self.color, self.species, self.legs)

sheep = SoundAnimals("white", 4, "manh manh")
print(sheep)
