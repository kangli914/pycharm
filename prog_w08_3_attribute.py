#creating attributes
class Car:
	' docstring: this subclass has a superclass'
	pass
	
# creating an object x of class Car
x=Car()

# adding new attributes to x
x.make="Toyota"
x.color="white"
x.year="2001"

print (x.color)

# Built-in class attributes. _dict__: accessing class dictionary of object attributes
print (x.__dict__)
print (x.__doc__)
'''
white
{'year': '2001', 'color': 'white', 'make': 'Toyota'}
 docstring: this subclass has a superclass
'''