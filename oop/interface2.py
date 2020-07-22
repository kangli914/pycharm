from abc import ABC, abstractmethod

class Shape(ABC):
    """Shape interface or abstract class (?) # https://www.youtube.com/watch?v=PDMe3wgAsWg
    acheive 2 things:
    - Do not want to user to creat a instance of Shape supper class
    - Whoever the subclass use the shape class, it implements the area and perimeter method. abstractmethod will do this job
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


# shap = Shape()
## once you @abstractmethod decorator on one of method, the class will become abstract class
## this way you will enforce user wont initiate a abstract class
## error:
##  abstractmethod is a method which you must implement in the sub class
##  File "/home/perfeng/repo/personal/pycharm/oop/interface2.py", line x, in <module>
##  shap = Shape()
##  TypeError: Can't instantiate abstract class Shape with abstract methods area

square = Square(5)
## whever subclass which inherites the an abstract class, subclass class have to implement those abstract methords in the subclass
## this way you enforce sub class to implement those abstract method otherwise it will generate the error
## error: 
##  File "/home/perfeng/repo/personal/pycharm/oop/interface2.py", line 32, in <module>
##  square = Square(5)
##  TypeError: Can't instantiate abstract class Square with abstract methods area, perimeter
print(f"Square area: {square.area()} and perimeter: {square.perimeter()}")