for letter in 'English':		# traversal of a string sequence
	print ('The current Leter is : ', letter)
print('\n')

colors = ('yellow', 'red', 'blue', 'black')
for color in colors:			# traversal of a List sequence
			print ('The current color is: ', color)
			print('\n')
print("This is an example of for in structure!")


for letter in 'English':		# traversal of a string sequence
		if letter == 'i':
			print ('there is letter: ', letter)
			break
else:print('we can\'t find a match letter!')