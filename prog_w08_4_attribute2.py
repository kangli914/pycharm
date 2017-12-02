#accessing attributes 
class Car:
	' docstring: this subclass has a superclass'
	pass

x=Car() # creating three attributes for instance x 
x.make="Toyota" 
x.color="white" 
x.year="2001" 
print (x.color) 
print (x.__dict__) # accessing the class dictionary
Car.model="Sienna" 
print (x.model) # will print Sienna 
x.model="Camry" 
print (Car.model) #will print Sienna 
print (getattr(x, 'model')) #another way to access attributes 
setattr(x, 'fuel','diesel') #creating a new attribute associated with a new value 
print (getattr(x, 'fuel')) 
print (x.__dict__) 
delattr (x,'fuel') # deleting the attribute fuel from x and the class dictionary 
print (x.__dict__) 
print (hasattr(x, 'fuel'))# checking if the attribute fuel exists in x
print (setattr(x, 'fuel', 'gas'))
print (x.__dict__) 

'''
white
{'make': 'Toyota', 'year': '2001', 'color': 'white'}
Sienna
Sienna
Camry
diesel
{'year': '2001', 'fuel': 'diesel', 'make': 'Toyota', 'color': 'white', 'model': 'Camry'}
{'year': '2001', 'make': 'Toyota', 'color': 'white', 'model': 'Camry'}
False
None
{'year': '2001', 'fuel': 'gas', 'make': 'Toyota', 'color': 'white', 'model': 'Camry'}
'''