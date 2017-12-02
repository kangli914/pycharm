def changeme (mylist):
	"This changes a passed list into this function"
	mylist = [1,2,3,4]						# This would assign new reference in mylist
	print ("Values inside the function: ", mylist)
	return mylist
	
# Now you can clal changeme function
mylist= [10,20,30]
changeme(mylist)
#mylist=changeme(mylist)   					# uncomment this line to see what happen 
print ("Value outside the function: ", mylist)