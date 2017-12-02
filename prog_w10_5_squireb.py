#using sub and quantifiers {} 

'''sub (patter, repl, string, max=0), max specifies the number of occurrences to be replaced.
'''

import re 
st =re.search (r"a{2,6}", "baaaaaafgb")   	   # a{2,6} repition of a from 2 to 6
st1 =re.search (r"a{2,6}?", "baaaaaafgb")   
if st: 
	print ( st.group()," :we found a match")   # output: aaaaaa  :we found a match --> gready search
	print ( st1.group()," :we found a match")  # output: aa  :we found a match	  --> minium search with (?)		
	
st2=re.sub (r"a{2,6}", "kkkkkk","baaaaaafgb")  # ? only matches 2 a's and replace them with 6 k's (gready search)
st3=re.sub (r"a{2,6}?", "kkkkkk","baaaaaafgb") # ? only matches 2 a's and replace them with 6 k's (minium search)

print (st2) 	# output: bkkkkkkfgb because of (gready search)						   
print (st3) 	# output: bkkkkkkkkkkkkkkkkkkfgb because of minium search


# replace any space (\s) or \( or \) with nothing (so remove () and space)
# output Phone Num :  01345656790
num = re.sub(r'[\s\(\)]', "", "(01)3456 567 90")
print ("Phone Num : ", num)