# creating a class with two instances
class Car:
	pass
car1=Car()
car2=Car()
car3=car2 		#car3 is alias for car2
print(car1);
print(car2);
print(car3);

'''
<__main__.Car object at 0x003BC630>
<__main__.Car object at 0x003BC6B0>
<__main__.Car object at 0x003BC6B0>
'''