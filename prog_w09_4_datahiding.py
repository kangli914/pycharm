# data hiding 
class MyCounter: 
	__hidenCount=0 
	
	def __init__(self,name="hello"): 
		self.name=name 
		print("initializing the object", self.name) 
		
	def count(self): 
		self.__hidenCount += 1;
		print (self.__hidenCount);
		
counter = MyCounter() 
counter.count() 
counter.count()
print("\n")
#print (counter.__hidenCount) 				# this will generate an error, hidenCounter can not be seen
#print (MyCounter.__hidenCount)				# AttributeError: type object 'MyCounter' has no attribute '__hidenCount'
print (counter._MyCounter__hidenCount)		# a special way to access the hidden variable: object._ClassName__HiddenClassVariable

'''
1
2


2
'''