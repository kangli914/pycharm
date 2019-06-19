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
- Python variables do not require explicit declaration to reserve memory location. Declaration of variables is not required in Python
  The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables

- Python Data structure
	1. List is a collection which is ordered and changeable. Allows duplicate members. []
	2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
	3. Set is a collection which is unordered and unindexed. No duplicate members. {}
	4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
	
## Operators:
1. Comparison operators: '==' & '!=' compare value. Identity Operators: 'is' & 'is not' compare object
	rule is to choose between == and is based on what kind of check you want. 
	If you care about the strings being equal (that is, having the same contents) then you should always use ==. 
	If you care about whether any two Python names refer to the same object instance, you should use is. 
	https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe
2. Logical Operators:  'and' & 'or' & 'not' return python Boolean 'True' or 'False'
3. Membership Operators: 'in' & 'not in': Evaluates to 'True' if it finds a variable in the specified sequence and 'False' otherwis
   sometimes, this is used in for-loops:
	```
	for x in list: (still condsidered as 'Membership' some sort)
	```
4. note: not such thing 'A is in'

## range([start], stop[, step])
1. Python for loop does NOT require an indexing variable(e.g. option 2) to set beforehand. so if need index, range() function will does the job (option 1):
	```
	OPTION 1)
	b='Python'
	for idx in range(len(b)):
		print(idx, b[idx])
	0 P
	1 y
	2 t
	3 h
	4 o
	5 n
	```
	above more like java style for loop with (int idx=0; idx < len(b); idx++)...
	VS.
	use build in to access element directly without index need
	```
	OPTION 2)
	b = 'Python'
		for idx in b:
		print(idx)
	P
	y
	t
	h
	o
	n
	```
	
2. range([start], stop[, step]) function returns a sequence of numbers.
	- start:starting from 0 by default, 
	- step: increments by 1 (by default), 
	- stop: at a specified number.but not including this number.
	can use negtive number to reverse - look at Option 4) in String section below

## String
* Python String: list --> https://www.programiz.com/python-programming/methods/string
1. substring: [return string]
	- string[start:end]: Get all characters from index start to end-1 (Note - exclude 'end')
	- string[:end]: Get all characters from the beginning of the string to end-1
	- string[start:]: Get all characters from index start to the end of the string
	- string[start : end : step]: Get all characters from start to end-1 discounting every step character
   
   NOTE - substring wont change original string
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
	```
	
	use for reverse pring string:
	```
	Option 1): using slice() - note: can use not only string but other collections like list and etc.
	>>> b='Python'
	>>> slice(-1,-1-len(b),-1)
	slice(-1, -7, -1)
	>>> x=slice(-1,-1-len(b),-1)
	>>> b[x]
	'nohtyP'

	Option 2): using `substring` to reverse
	>>> print(b[-1::-1])
	'nohtyP'
	
	Option 3): for loops using explicit idx (e.g. without range())
	>>> b='Python'
	>>> idx=0
	>>> a=''
	>>> for ch in b:
	...     a+=b[-1-idx]  || a+=b[len(b)-1-idx]
	...     idx=idx+1
	...
	>>> print(a)
	nohtyP
	
	Option 4): for loops with range() (simpler than Option 2. note range 'end' not include the end indx)
	>>> b='Python'
	>>> a=''
	>>> for idx in range(-1, -1-len(b), -1):
	>>> 	a+=b[idx]
	>>> print (a)
	nohtyP
	```
	ref: https://www.programiz.com/python-programming/methods/built-in/slice
	
5. convert:
	- .lower(), .upper()... 	
	
	
   refer: https://www.w3schools.com/python/python_strings.asp
		  https://www.programiz.com/python-programming/methods/string
		  https://stackoverflow.com/questions/13783934/what-does-s-strip-do-exactly [.strip()]

## List
methods modify original list:
1. Add item: list.append(x), list.insert(i, x)
2. Remove item:  list.remove(x) [only remove first matching item not all],   list.pop([i])
3. Order: sort(), reverse() 
4. Clone: copy(). note: x=[a,b,c], x=y both x,y refer to the same list
5. Find/Search: index(sub[, start[, end]])
7. Count: .count(x)
6. use as:
	Stack: 	[last-in, first-out]: 	.append(x), .pop()
	Queues: [first-in, first-out]:  .append(x), .pop(0)

execise code: https://github.com/kangli914/pycharm/blob/master/dummy/list_dummy.py


## File Path
import os

## OS.Path

input_dir = "Z:\\Workspaces\\GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33"
print(os.path.normpath(input_dir)) 
```Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33```

print(os.path.abspath(input_dir)) 
``` Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33```

print(os.getcwd()) 
``` C:\workspace\_github\pycharm\dummy```

print(os.path.dirname(input_dir))

print(os.path.basename(input_dir))

``` Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results```

``` N_2019-05-17_08-33```

print(os.path.join(os.path.dirname(input_dir),os.path.basename(input_dir)))
``` Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33```

print(input_dir.rsplit("\\", 1)[1])
``` N_2019-05-17_08-33```


``` split file and extention: e.g. dummy && .txt ```
file = "dummy.txt"
root, ext = os.path.splitext(file)
print(root, ext)

``` to walkthrought a directory ```
for root, dirs, files in os.walk("C:\\workspace\\_github"):
    for file in files:
        print("file name:", os.path.join(root, file))
    for dir in dirs:
        print("dir name:", os.path.join(root, dir))
	

## Time
*time.time():*
```
print("time.time() in seconds:", time.time(), "type:", type(time.time()))
time.time() in seconds: 1560964870.9869883 type: <class 'float'>
```
*Representation betwen time (local, UTC) and epoch:*

1. time.gmtime([epoch_secs]): from 'seconds since the epoch' (if not specify time()) to 'struct_time in UTC'
2. time.localtime([epoch_secs]): from 'seconds since the epoch' (if not specify time()) to 'struct_time in local time'
3. time.calendar.timegm(t): from 'struct_time t in UTC' to 'seconds since the epoch' (inverse function of time.gmtime)
4. time.mktime(t): from 'struct_time t in local time' to 'seconds since the epoch' ( inverse function of localtime())
	```
	Local time: Wed Jun 19 14:47:18 2019
	print("time.gmtime():", time.gmtime())
	print("time.localtime():", time.localtime())

	time.gmtime(): time.struct_time(tm_year=2019, tm_mon=6, tm_mday=19, tm_hour=18, tm_min=47, tm_sec=18, tm_wday=2, tm_yday=170, tm_isdst=0)
	time.localtime(): time.struct_time(tm_year=2019, tm_mon=6, tm_mday=19, tm_hour=14, tm_min=47, tm_sec=18, tm_wday=2, tm_yday=170, tm_isdst=1)

	# once in 'struct_time' it access element by .tm_year
	print("time.gmtime().tm_year:", time.gmtime().tm_year)
	time.gmtime().tm_year: 2019
	https://www.programiz.com/python-programming/time
	```
*time.asctime([t]):*

Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string
```
print(time.asctime(time.gmtime(1560973263)), type(time.asctime(time.gmtime(1560973263))))
print(time.asctime(time.localtime(1560973263)), type(time.asctime(time.localtime(1560973263))))
Wed Jun 19 19:41:03 2019 <class 'str'>
Wed Jun 19 15:41:03 2019 <class 'str'>
```
**so Convrting time from epoch to str in both UTC and Local:**
1. use gmtime(epoch), localtime(epoch) to convert epoch to 'struct_time' object
2. then use ascttime(t) convert 'struct time' to string

or

Converting 'local' time only from epoch to str directly without going through 'struct_time' using 'time.ctime()' below:


*time.ctime(epoch_secs):*

Purpose was similar to 'time.localtime': epoch to time but 'str' directly instead of via 'struct_time'
```
print("time.ctime():", time.ctime(1560973263), "type:", type(time.ctime(1560973263)))
time.ctime(): Wed Jun 19 15:41:03 2019 type: <class 'str'>
```





	
