import math 
mytup= (8,'good','soccer', 37.5,'player',9,)
mytup1= ('good','soccer', 37.5,'player',9,8) 
mytup2= ('beginner', 7,'car', 44, 'driver',12) 
mytup3= (4, 5, 0, 9) 
mytup4= ('a','cab','ac','cc', 9999) 
mytup5= ('a','cab','ac','cd') 
print (mytup[1:3]) 
print (mytup2[2:]) 
print (len(mytup)) 
print (mytup + mytup2) 
print (mytup * 3) 
print ('good' in mytup) 
print (max (mytup3)) 
#print (min (mytup4))
#print (sorted(mytup4)) 
d = (mytup == mytup4) 
print (d)
d2 = (mytup == mytup1)
print (d2)

d3 = (mytup4 < mytup5)
print (d3)	# return true because 'cc' in mytup4  is before 'cd' in mytup5. it compare the order of letters than # lenth of tuple

d4 = (mytup4 == mytup5)
print (d4)	