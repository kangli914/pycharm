salary=int(input("Entry your salary: "))
yearOnJob=int(input("Enter years of experience: "))

if salary<=3000:
	if yearOnJob>=3:
	 print("You quality for a loan")
	else:
					print ("You quality for a half of a loan")
else:
	if yearOnJob>=10:
		  print("You quality for a half of a 25% loan")
	else:
		       print ("You do not quality for loans")	