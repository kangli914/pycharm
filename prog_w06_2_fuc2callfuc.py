'''
Point # 1 - Changes occur to the passed values only seen inside the function. (passing 'value' as opposite to passing by 'reference')
Point # 2 - We can make the changes visible outside the function by assigning 
the returned value from the function to the passed value within the main function.
'''

def main():
	value=10
	changevalue(value);
	print ('The value is', value) 			# p#1 - Changes occur to the passed values only seen inside the function.
	value=changevalue(value)
	print ('The value 2nd time is', value)	# p#2 - We can make the changes visible outside the function by assigning 
											# the returned value from the function
	
def changevalue(value):
	value=50
	value=value+10;
	return value;

#calls main
main()