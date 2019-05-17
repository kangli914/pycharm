# Python notes:

## General:
- Python Data type: Numbers, String, List, Tuple, Set, Dictionary
- print
	```
	>>> print("abc:", "cde")
	abc: cde
	>>> print("abc:"+ "cde")
	abc:cde
	>> print("abc:{}".format("cde"))
	abc:cde
	```
- Python variables do not require explicit declaration to reserve memory location. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables
-
	1. List is a collection which is ordered and changeable. Allows duplicate members. []
	2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	3. Set is a collection which is unordered and unindexed. No duplicate members.
	4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
	
## Operators:
1. Comparison operators: '==' & '!=' compare value. Identity Operators: 'is' & 'is not' compare object
2. Logical Operators:  'and' & 'or' & 'not' return python Boolean 'True' or 'False'
3. Membership Operators: 'in' & 'not in': Evaluates to 'True' if it finds a variable in the specified sequence and 'False' otherwis
4. note: not such thing 'A is in'

## String
* Python String: list --> https://www.programiz.com/python-programming/methods/string
1. substring: [return string]
	- string[start:end]: Get all characters from index start to end-1 (Note - exclude 'end')
	- string[:end]: Get all characters from the beginning of the string to end-1
	- string[start:]: Get all characters from index start to the end of the string
	- string[start:end:step]: Get all characters from start to end-1 discounting every step character
   
   refer: https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/

2. 	assert: [return Boolean]
	- .islower(), .isupper(), .isalpha(), .isalnum(), [.isdecimal() < .isdigit() < isnumeric() (containing decimal, digit)]
	- .isspace(): Characters that are used for spacing are called whitespace characters. For example: tabs, spaces, newline etc. Return True if *all* characters (only whitespace)in the string are whitespace characters


3. search: [return index]
	- .index(sub[, start[, end]]) & .find(sub[, start[, end]]) both return lowest index of matching substring takes 3 params. substring, start(optional), end (optional). except substring doesnt exist return -1 for find() vs. index return exceptions
		1. It's the substring to be searched in the str string.
		2. start and end (optional) - substring is searched within str[start:end]
		- .rfind(sub[, start[, end]]) find the hight index of matching substring (from right most)
		usage example:
		```
		# How to use find()
		if  (quote.find('be,') != -1):
		  print("Contains substring 'be,'")
		else:
		  print("Doesn't contain substring")
	```
	- .startswith(prefix[, start[, end]]) & .endswith(suffix[, start[, end]]): Return True/false to checksif String Starts/ends with the Specified String. params: start & end are optional
	- .counts(sub[, start[, end]]): returns the number of occurrences of a substring in the given string.
	
4. replace: [return string]
	- .replace(old, new [, count]):  returns a copy of the string where all occurrences of a substring is replaced with another substring.
	   1. count (optional) - the number of times you want to replace the old substring with the new substring
	   2. If count is not specified, replace() method replaces all occurrences of the old substring with the new substring.
	
5. remove: [return string]
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
	- .rstrip([chars]): returns a copy of the string with trailing characters removed (based on the string argument passed).
	
6. split: [return a list]
	- .split([separator [, maxsplit]]) :	Splits String from Left
		1. Separator (optional)- The is a delimiter. The string splits at the specified separator. If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
		2. maxsplit (optional) - The maxsplit defines the maximum number of splits. The default value of maxsplit is -1, meaning, no limit on the number of splits.
	    If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
		
		```
			>>> a = 'Milk, Chicken, Bread'
			>>> left=a.split(', ', 1)[0]
			>>> right=a.split(', ', 1)[1]
			>>> print(left, right)
			Milk Chicken, Bread
			>>> print(left)
			Milk
			>>> print(right)
			Chicken, Bread
		```
	- .rsplit([separator [, maxsplit]]): plits string from the Right, at the specified separator and returns a list of strings.
	- .splitlines() : The splitlines() method splits the string at line breaks and returns a list of lines in the string.
	
7. slice: [return string] - not ONLY apply string, The slice object is used to slice a given *sequence* (string, bytes, tuple, list or range)
	start - starting integer where the slicing of the object starts
	stop - integer until which the slicing takes place. The slicing stops at index stop - 1. [if spacify, then it will be `stop` then `start']
	        e.g. 
			slice[stop] or
			slice[start, stop] or
			slice[start, stop, step]
			
	step - integer value which determines the increment between each index for slicing. using '-1' to become reverse, e.g. from right to left
	```
	>>> b='Python'
	>>> slice(3)
	slice(None, 3, None)
	>>> type(slice(3))
	<class 'slice'>
	>>> x=slice(3)
	>>> b[x]
	'Pyt'
	
	>>> b='Python'
	>>> x=slice(1,5,2)
	>>> type(x)
	<class 'slice'>
	>>> b[x]
	'yh'

	>>> b='Python'	
	>>> x = slice(-1, -4, -1)
	>>> b[x]
	'noh'
	
	use for reverse pring string:
	>>> b='Python'
	>>> slice(-1,-1-len(b),-1)
	slice(-1, -7, -1)
	>>> x=slice(-1,-1-len(b),-1)
	>>> b[x]
	'nohtyP'
	
	```
	ref: https://www.programiz.com/python-programming/methods/built-in/slice
	
5. convert:
	- .lower(), .upper()... 	
	
	
   refer: https://www.w3schools.com/python/python_strings.asp
		  https://www.programiz.com/python-programming/methods/string
		  https://stackoverflow.com/questions/13783934/what-does-s-strip-do-exactly [.strip()]