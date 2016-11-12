class SchoolMember: 
	'Represents any school member.' 
	def __init__(self, mName, mAge): 
		self.name = mName;
		self.age = mAge;
		print('(Initialized SchoolMember: {})'.format(self.name)) 
		
	def tell(self): 
		'Tell my details.' 
		print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ") 
		
class Teacher(SchoolMember): 
	'Represents a teacher.' 
	def __init__(self, name, age, salary): 				# overriding super init method
		SchoolMember.__init__(self, name, age) 
		self.salary = salary 
		print('(Initialized Teacher: {})'.format(self.name)) 
		
	def tetell(self): 
		self.tell() 									# two ways of calling the same methord: self.tell() = SchoolMember.tell(self) 
		#SchoolMember.tell(self) 
		print('Salary: "{:d}"'.format(self.salary)) 
		
class Student(SchoolMember): 
	'Represents a student.' 
	def __init__(self, name, age, mark):				# overriding super init method
		SchoolMember.__init__(self, name, age) 
		self.mark = mark 
		print('(Initialized Student: {})'.format(self.name)) 

	def sttell(self): 
		#self.tell() 			
		SchoolMember.tell(self)						    # two ways of calling the same methord: self.tell() = SchoolMember.tell(self)
		print('Mark: "{:d}"'.format(self.mark))

t = Teacher("Mrs. Shrivi",40,30000) 
s = Student("Swaroop",25,75) 
# prints a blank line 
print() 
t.tetell() 
s.sttell()

'''
(Initialized SchoolMember: Mrs. Shrivi)
(Initialized Teacher: Mrs. Shrivi)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrivi" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Mark: "75"
'''

members = [t,s]  # a list of objects t and salary
for member in members:
	print ("List loop: ", member.tell())