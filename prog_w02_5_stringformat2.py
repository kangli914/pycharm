instructor = input('Enter the prof name: ')
subject = input("Enter the subject name: ")
term = input("Enter the term name: ")
year ="1998"
numberBraces ="{0} will teach {1} in {2}."
print (numberBraces.format (instructor, subject, term))
print (numberBraces.format (subject, year, instructor))