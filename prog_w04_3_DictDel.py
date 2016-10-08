myDict = {'Name': 'Fahim', 'Age':7}
print (myDict)
print (str(myDict))			# Str() returns the string representation of a dictionary which is same as line # 2
del myDict['Name']			# remove entry with key 'Name'
print (myDict)
myDict.clear()				# remove all entries in dict; other words make it empty dict. it still will exist
print ("Empty dictonary: ? yes", myDict)

myDict ['empName'] = 'Simon'# or using 'setdefault' method
print (myDict)


del (myDict)				# Delete the entire dictonary
print (myDict)				# since dictonary is deleted, then you get error: 'myDict' is not defined