'''
The __init__ is an important method in Python and usually called immediately after the class definition. The name is fixed and can not be changed. 
This method is similar to constructors in Java and C#. It is called when an instance is created so its job is to initialize that instance with data we want.

Self: class methods in Python have a special arguments added as a first arg in the argument list. We do not pass a value to it as Python provides it. 
The (self) is there to refer to the object itself. This is important so we know to which object the initialization was triggered (there could be multiple objects are initialized using the same __init__). It is recommended to keep the name as (self), just like Java which uses (this).
'''

#working wiht __init__ method
class Library:
	def __init__(self, name):
		self.name = name  		# '__init__' method is similar to constructors in Java. self --> object 'p' and 'q'
	def greeting(self):			# (self) just like Java which uses (this).  
		#if self.name:
			print('Hello, you are in', self.name, 'library')
		#else:
			#print ("forgot to provide the library name")

p = Library('Fairview')			# Creating and initilziing the object e.g this(= self).name = 'Fairview'
p.greeting();
q=Library('')
q.greeting()

'''
Hello, you are in Fairview library
Hello, you are in  library
'''