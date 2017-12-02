# pattern/quantifiers
import re 
mylist=["Ji Neuk","I Neu", "Jo Nu"] 
for x in mylist: 
	if re.search (r"J.* Neu", x): 
		print (x, " has the string") 
	else: 
		print (x, "does not have the string")