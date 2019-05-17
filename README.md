# Python notes:

* Operators:
1. Comparison operators: '==' & '!=' compare value. Identity Operators: 'is' & 'is not' compare object
2. Logical Operators:  'and' & 'or' & 'not' return python Boolean 'True' or 'False'
3. Membership Operators: 'in' & 'not in': Evaluates to 'True' if it finds a variable in the specified sequence and 'False' otherwis
4. note: not such thing 'A is in'

* Python Data type: Numbers, String, List, Tuple, Dictionary

* Python String: list --> https://www.programiz.com/python-programming/methods/string
1. substring:
	- string[start:end]: Get all characters from index start to end-1
	- string[:end]: Get all characters from the beginning of the string to end-1
	- string[start:]: Get all characters from index start to the end of the string
	- string[start:end:step]: Get all characters from start to end-1 discounting every step character
   
   refer: https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/

2. remove:
	- .strip([chars]): if char not provided, the method removes any whitespace from the beginning or the end; can pass character. 
					   if char is passed, it will search all the char of the set one by one form left and right side of the target string.
					   If a char in the string s isn't in the set than *no further* checking is done form that side and stop from that side
					   searching will be continue from the other side till similar thing is happen form that side. 
					   if char in string s is found in set than that char is removed and continue
					   example:
					   s="this is tricky"; s.strip("thsy") output: 'is is trick'
					   1) make 'thsy' as char set - B [t,h,s,y]
					   2) search char A by char from most-left and most left
						- if char A is in B, found and removed and continue
						- else chart A is not in B, not found and stop
					   
	- .lstrip([chars]): removes characters from the left based on the argument (a string specifying the set of characters to be removed).
	
3. search and find:
	- .index() & .find() both return lowest index of matching substring takes 3 params. substring, start, end (optional). except substring doesnt exist return -1 for find() vs. index return exceptions
	1. It's the substring to be searched in the str string.
	2. start and end (optional) - substring is searched within str[start:end]
	- .rfind() find the hight index of matching substring
	usage example:
	```
	# How to use find()
	if  (quote.find('be,') != -1):
	  print("Contains substring 'be,'")
	else:
	  print("Doesn't contain substring")
	```

4. 	
	- .lower(), .upper(), .islower(), .isupper()
	- .replace("H", "J"):  replaces a string with another string
	- .split(","): plits the string into substrings if it finds instances of the separator
	
   refer: https://www.w3schools.com/python/python_strings.asp
		  https://www.programiz.com/python-programming/methods/string
		  https://stackoverflow.com/questions/13783934/what-does-s-strip-do-exactly [.strip()]