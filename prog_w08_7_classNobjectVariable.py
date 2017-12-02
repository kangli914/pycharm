#looking into class variable and instance variables 
class Student: 
	"Common base class for all students"
	stuCounter = 0 # this is a class variable: is defined outside methods but inside a class

	def __init__(self, name, mark): 
		self.name = name 
		self.mark = mark 
		Student.stuCounter += 1
		
	def dispStudent(self): 
		print ("Student : ", self.name, ", Mark: ", self.mark)
	
#creating a first object of Student class 
student1 = Student("John", 91) 
#creating a second object of Student class 
student2 = Student("Diana", 94)

student1.dispStudent()
student2.dispStudent() 
print ("Total number of students %d" % Student.stuCounter)

'''
Student :  John , Mark:  91
Student :  Diana , Mark:  94
Total number of students 2
''''