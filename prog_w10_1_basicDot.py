#re basic patterns

''' ref#1: https://docs.python.org/3/library/re.html
'' ref#2: https://www.debuggex.com/cheatsheet/regex/python  (Python Regex Cheatsheet)
'' go to 'prog_w10_3_wordNgroup.py' 

'' the 'r' in r".at" here means if you have \n included in string , it will convert to a regular string (as '\n') than new line. so it will print as "\n"
'''

import re 
#using dot to search 
if re.search (r".at", "rat"): 
	#if re.search (r".*at", "rcat"): 
	#if re.search (r".at", "at"): 		# error 
	print ("a match has been found") 
else: 
	print (" no match has been found")