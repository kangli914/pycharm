months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
beforeGreen =[0]*12
afterGreen =[0]*12
savingAmount =[0]*12

def output2file(months, beforeGreen, afterGreen, savingAmount, output_filename):
	with open(output_filename, 'w') as output_file:
		for index in range(len(months)):
			tmpString = months[index] + "\t" + str(beforeGreen[index]) + "\t" + str(afterGreen[index]) + "\t" + str(savingAmount[index]) + "\n"
			#print("%s" % (tmpString))
			output_file.write(tmpString)
	output_file.close()

def readBillBeforeGreen(months, beforeGreen):
	for index in range(len(months)):
		print ("month %s" % (months[index]) )
		beforeGreen[index] = int(input("Enter the bill before green program? "))

def readBillAfterGreen(months, afterGreen):
	for index in range(len(months)):
		print ("month %s" % (months[index]) )
		afterGreen[index] = int(input("Enter the bill after green program? "))


def calcBillDifference(months, beforeGreen, afterGreen, savingAmount):
	for index in range(len(months)):
		savingAmount[index] = afterGreen[index] - beforeGreen[index]
		print ("month index: %s - netSaving amount: %s" % (index, savingAmount[index]))

def displaySaving(months, beforeGreen, afterGreen, savingAmount):
	for index in range(len(months)):
		print ("%s: %s: %s: %s \n" % (months[index], beforeGreen[index], afterGreen[index], savingAmount[index])) 
		



readBillBeforeGreen(months, beforeGreen)
readBillAfterGreen(months, afterGreen)		
calcBillDifference(months, beforeGreen, afterGreen, savingAmount)
displaySaving(months, beforeGreen, afterGreen, savingAmount)
output2file(months,beforeGreen,afterGreen,savingAmount,"outfile.txt")

'''
Last year, a local college implemented rooftop gardens as a way to promote energy efficiency and save money. Write a program that will allow the user to enter the energy bills from January to December for the year prior to going green. Next, allow the user to enter the energy bills from January to December of the past year after going green. The program should calculate the energy difference from the two years and display the two years worth of data, along with the savings. Additionally, the savings array should be printed to a file called savings.txt.
'''