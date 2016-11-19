'''
'' \w - Match a single word character: [A-Za-z0-9_]
'' group (num): returns the entire match or matching subgroups
   - group(0) return entire match
   - group(1) return 1 matched subgroups
   - group(2) return 2 matched subgroups
   
Match function returns a match object on success, None for no match results. 
It checks at ******the beginning of the string ONLY *****.
But Search is looking for the entire string for a match

search ⇒ find something anywhere in the string and return a match object.

match ⇒ find something at the beginning of the string and return a match object.
	
'''
import re 
#using match and grouping the result 
m = re.match(r"(\w+) (\w+)", "Isaa_g1 Iswton_g2, jjhuyt") 
print(m.group(0)) 
print(m.group(1)) 
print(m.group(2))