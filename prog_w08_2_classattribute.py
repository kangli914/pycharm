#working wiht built in class attributes
class Vehicle:
	pass
class Car(Vehicle):
	'This is class documentation string can be accessed by calling calss Built-in class attributes __doc__'
	pass
class Van(Car):
	'This is Van, a subclass of Car'
	pass

#accessing built-in class attributes
print("Car.__doc__:", Car.__doc__);
print("Car.__name__:", Car.__name__);

"""__module__: accessing the module name in which the class is defined."""
print("Car.__module__:", Car.__module__);

print("Car.__bases___:", Car.__bases__);

print("Van.__doc__:", Van.__doc__);
print("Van.__name__:", Van.__name__);
print("Van.__module__:", Van.__module__);
print("Van.__bases___:", Van.__bases__);


'''
Car.__doc__: This is class documentation string can be accessed by calling calss Built-in class attributes __doc__
Car.__name__: Car
Car.__module__: __main__
Car.__bases___: (<class '__main__.Vehicle'>,)
Van.__doc__: This is Van, a subclass of Car
Van.__name__: Van
Van.__module__: __main__
Van.__bases___: (<class '__main__.Car'>,)
'''