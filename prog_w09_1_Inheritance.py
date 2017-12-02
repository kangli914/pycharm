class Sup:
	superAttr = 1000    # class variable, visible out side of class
	def __init__(self):
		print ("Calling super initializer")
		
	def superMethod(self):
		print ("Calling super method")
		
	def setAttr(self, attr):
		self.superAttr = attr
		
	def getAttr(self):
		print("Super attribute :", self.superAttr)
		
class Sub (Sup):
	def __init__(self):
		print ("Calling sub initializer")
		
	def subMethod(self):
		print ("Calling sub method")

'''
Calling sub initializer
Calling sub method
Calling super method
Super attribute : 2000
'''
x=Sub()
x.subMethod()
x.superMethod()
x.setAttr(2000)
x.getAttr()

'''
Calling super initializer
Super attribute : 300
Accessing the class variable directly:  2000
Accessing the class variable directly:  300
'''
y=Sup()
y.setAttr(300)
y.getAttr()
print ("Accessing the class variable directly: ", x.superAttr)
print ("Accessing the class variable directly: ", y.superAttr)