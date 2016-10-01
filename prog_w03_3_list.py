#!/usr/bin/python3 
myList = [ 'Monday', 19 , 2000, 'is', 'forgotten' ] 
mySubList = [19,   'date', 0]
emptyList = [ ]
myList2 = ["Wednesday", 8]
print (myList) 					# Prints complete list 
print (myList [0]) 				# Prints first element of the list 
print (myList [2:4]) 			# Prints elements starting from 2nd till 3rd 
print (myList [3:]) 			# Prints elements starting from 3rd element 
print (mySubList * 2) 			# Prints list two times 
print (myList + mySubList) 		# Prints concatenated lists

myList [4]= "unforgotten"
print (" print an updated list", myList)
print (" print an empty list", emptyList)
print (myList + emptyList) 

#max(myList) 					# error
print (len ([1,3,4] + [5+6+7]))
del myList [4]
print ("MY LIST after deleting itme at index 4", myList)
print (2000 in myList) 			# Print True
print (myList.append(myList2))  # Print none - append only add object instead of list
print (myList.extend(myList2))