'''
Requriment: 
Write a program that will calculate the cost of purchasing a meal. This program will include decisions and loops. Details of the program are as follows:
 Your menu items only include the following food with the accompanying price:
o Yum Yum Burger = .99
o Grease Yum Fries = .79
o Soda Yum = 1.09
 Allow the user of the program to purchase any quantity of these items in one order.
 Allow the user of the program to purchase one or more types of these items in one order.
 After the order is placed, calculate total and add a 6% sales tax.
 Print to the screen a receipt showing the total purchase price.
'''

#Yum Yum Burger Joint 
#the main function 
def main(): 
	endProgram = 'no' 
	print() 
	while endProgram == 'no': 
		totalBurger = 0 
		totalFry = 0 
		totalSoda = 0 
		endOrder = 'no' 
		while endOrder == 'no': 
			print()
			print ('Enter 1 for Yum Yum Burger') 
			print ('Enter 2 for Grease Yum Fries') 
			print ('Enter 3 for Soda Yum') 
			option = input('Enter now ->') 
			#### here totalBurger, totalFry and totalSoda are passing by reference as oppoite to passing by value
			if option == '1': 
				totalBurger = getBurger(totalBurger)
			elif option == '2': 
				totalFry = getFry(totalFry)
			elif option == '3': 
				totalSoda = getSoda(totalSoda)
			else: 
				print ('You have entered an invalid option!!!') 
			endOrder = input('Do you want to end your order? (Enter yes or no): ') 
		print() 
		total = calcTotal(totalBurger, totalFry, totalSoda)
		printReceipt(total) 
		
		endProgram = input('Do you want to end program? (Enter no to process a new order): ') 
		
#this function will get burger order 
def getBurger(totalBurger):
	cnt = int(input("Enter the number of burgers you want: ")) 
	return totalBurger+cnt*0.99 

#this function will get fry order 
def getFry(totalFry): 
	cnt = int(input("Enter the number of fry you want: " )) 
	return totalFry+cnt*0.79
	
def getSoda(totalSoda): 
	cnt = int(input("Enter the number of sode you want: ")) 
	return totalSoda+cnt*1.09
	
def calcTotal(totalBurger, totalFry, totalSoda): 
	return totalBurger+totalFry+totalSoda
	
def printReceipt(total): 
	print ('The total price is $', total) 
	
# calls main 
main()