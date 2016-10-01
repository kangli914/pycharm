list1 = ['physics', 'Chem', 'Maths']
print ('list1 is:', list1)
list2=list(range(5)) 			# creates list of numbers between 0-4

list1.extend("7")
list1.extend(list2)				# Appends list to list
print ('list1 after extend', list1)
list1.append("6")				# Appends element to list
list1.append([8])
print ("list1 after append", list1)

list1.extend("7")
print (list1)		
list1.append(list2)
print (list1)