import re 

if re.search (r"Dec(ember)?\s", "I am going to meet him on December 18 2016"): 
	print ("a match has been found") 
else: 
	print (" no match has been found")
	
	
'''
re.search (r"Dec(ember)?\s", "I am going to meet him on December18 2016"): 
--> no match has been found (as there is no space between r and 18)


if re.search (r"Dec(ember)?\s", "I am going to meet him on December 18 2016"):
--> a match has been found
'''