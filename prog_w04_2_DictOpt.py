#!/user/bin/python3
dict1 = {'Name': 'Fahim', 'Age':7}
dict2 = {'Name': 'Rana', 'Age':7}
dict3 = {'Name': 'Fahim', 'Age':37, 'Tel': '555555'}
mySubTuple =('October', 2016, 21.5)
print (len (dict1))
print (dict1 != dict2)
print (str(dict1))
print(dict1)
print(type (dict1))
print(type (mySubTuple))
print(dict1.keys())
print(dict1.values())
dict1.update(dict3)
print (dict1)
dict4=dict1.copy()
print(dict4)
print(dict1 == dict4)
print (dict2.get('Age'))
print (dict2.get('title'))
dict3.setdefault('Sex', 'm')
dict3.setdefault('Age', None)
dict2.setdefault('Age', None)
print(dict3)
print(dict2)