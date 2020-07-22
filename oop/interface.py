# from abc import ABC
import abc

# class TrafficLight(abc.ABC):
class TrafficLight(abc.ABC):
    "Trafic Interfaces"

    @abc.abstractmethod
    def red(self):
        pass

    def yellow(self):
        pass

    def green(self):
        pass

class TrafficNA(TrafficLight):
    "sub class"

    def __init__(self, color):
        self.color = color
    
    def red(self):
        print(f"color is {self.color} - stop")

    def yellow(self):
        print(f"color is {self.color} - slow down")

    def green(self):
        print(f"color is {self.color} - move on")


list = [TrafficLight(), TrafficNA("red")]
for i in list:
    print(f"{i.red()}")

