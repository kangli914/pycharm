# deleting (destroying) an object 
class AnObject: 
	def __init__( self, x=0, y=0): 
		self.x = x 
		self.y = y 
		
	def __del__(self): 
		print ("object is deleted") 
		
ob1 = AnObject() 
ob2 = ob1 
ob3 = ob1 
print (id(ob1), id(ob2), id(ob3)) # prints the ids of the objects 


'''
2868912 2868912 2868912
object is deleted
'''
del ob1 
#del ob2 
del ob3