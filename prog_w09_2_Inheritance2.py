class ShoeFactory: 
	def __init__(self, skind, scode): 
		self.shoetype = skind 
		self.shoecode = scode 
	
	def typeDescription(self): 
		return (self.shoetype + " : " + self.shoecode) 
		
class Shoe(ShoeFactory): 
	def __init__(self, kind, code, color):     				# overriding super init method
		ShoeFactory.__init__(self, kind, code) 				# inheriting the attributes (kind, code) that were defined in the super class
		self.shoecolor = color 
		
	def getShoeColor(self): 
		return (self.typeDescription() + " : " + self.shoecolor) 
	
x = ShoeFactory("boots", "111111") 
y = Shoe("sport", "555555", "brown") 

'''
boots : 111111
sport : 555555 : brown
Accesing class variable directly:  brown
sport : 555555
'''
print(x.typeDescription())
print(y.getShoeColor())
print("Accesing class variable directly: ", y.shoecolor)
print(y.typeDescription())