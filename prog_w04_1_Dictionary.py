'''
5 Data types in Python:
* Numbers 		--> Immutable
* String  		--> Immutable
* List    		--> Mutable
* Tuple   		--> Immutable
* Dictionary	--> Key Immutable (Numbers, String, Tuple)
				--> Value Mutable
'''


# Keys are immutable; they accept data types such as string, integer or tuples.
myDict = {"empName": 'Simon', "title": "Director", "yOfEmp": 8} 
print ("myDict['empName']: ", myDict["empName"]) 
print ("myDict['title']: ", myDict["title"])

myDict3 = {['empName']: 'Simon', 'title': 'Director', 'yOfEmp': 8}	
'''
the keys are immutable; they accept data types such as string, integer or tuples. 
here you will get error: like "unhashable type: 'list' since the key is 'list' and list is mutable
e.g. a list is a mutable data type i.e. this type can be altered
Note that you can use only immutable objects (like strings) for the keys of a dictionary but you can use
either immutable or mutable objects for the values of the dictionary. This basically translates to say that
you should use only simple objects for keys.

there is no order in dictionary
'''
print (myDict3['title'])