student = input("Enter student name: ")
greeting='Hello,{}!'.format(student)
print(greeting)

greeting2='Hello,{}_AND_{}!'.format(student, "Ethan")
print(greeting2)


greeting3='Hello,{2}, {0}, {1}!'.format("kang1","kang2","kang3")
print(greeting3)

greeting4='{:.2}'.format('xylophone')
print(greeting4)

'''
look for more example in url: https://pyformat.info/
'''