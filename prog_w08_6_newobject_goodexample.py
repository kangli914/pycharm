#working wiht __init__ method
class Library:
	def __init__(self, name):
		self.name = name  		# '__init__' method is similar to constructors in Java. self --> object 'p' and 'q'
	def greeting(self):			# (self) just like Java which uses (this).  
		#if self.name:
			print('Hello, you are in', self.name, 'library')
		#else:
			#print ("forgot to provide the library name")
	def displaybook(self, bookname):	
		print("The book I borrowed from the library %s is: %s"%(self.name, bookname))
			
			
p = Library('Fairview')			# Creating and initilziing the object e.g this(= self).name = 'Fairview'
p.greeting();
q=Library('')
q.greeting()

b=Library('Dundus Street')
b.displaybook("<book title: Pathon Programming 101>")

'''
Hello, you are in Fairview library
Hello, you are in  library
The book I borrowed from the library Dundus Street is: <book title: Pathon Programming 101>
'''