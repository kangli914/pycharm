
# Python notes

## General

- Python Data type: Numbers, String, List, Tuple, Set, Dictionary:
<https://realpython.com/python-data-types/#strings>

  ```
  >>> type(10)
  <class 'int'>
  >>> type(10.1)
  <class 'float'>
  
  >>> type('I am too.')
  <class 'str'>

  # Note - None is not a str type
  >>> type(None)
  <class 'NoneType'>

  >>> type(True)
  <class 'bool'>
  >>> type(TRUE)
  NameError: name 'TRUE' is not defined

  # Note - anything numbers and string except 0 and None will be True
  >>> bool('abc')
  True
  >>> bool(2)
  True
  >>> bool(-1)
  True

  # zero, None(object) and empty string are False
  >>> bool(0)
  False
  >>> bool(None)
  Flase
  >>> bool('')
  Flase
  ```  

- print

 ```
 >>> print("abc:", "cde")
 abc: cde
 >>> print("abc:"+ "cde")
 abc:cde
 >> print("abc:{}".format("cde"))
 abc:cde
 ```

- Python variables do not require explicit declaration to reserve memory location. Declaration of variables is not required in Python
  The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables

- Python Data structure

 1. List is a collection which is ordered and changeable. Allows duplicate members. []
 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()

 note:
 Tuple is generally used when you want to pass a dataset which you don't want to other subfunction to modify or you are not sure if sub-function will/will not modify so you want to enfore the rule of no change to the dataset

 3. Set is a collection which is unordered and unindexed. No duplicate members. \{}
 4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
 5. Pthon sequences: strings, lists and tuple

## Operators

1. Comparison operators: '==' & '!=' compare value. Identity Operators: 'is' & 'is not' compare object
 rule is to choose between == and is based on what kind of check you want.
 If you care about the strings being equal (that is, having the same contents) then you should always use ==.
 If you care about whether any two Python names refer to the same object instance, you should use is.
 <https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe>
2. Logical Operators:  'and' & 'or' & 'not' return python Boolean 'True' or 'False'
3. Membership Operators: 'in' & 'not in': Evaluates to 'True' if it finds a variable in the specified sequence and 'False' otherwis
   sometimes, this is used in for-loops:

 ```
 for x in list: (still condsidered as 'Membership' some sort)
 ```

4. note: not such thing 'A is in'

## Arguments

There are two type of arguments:

1. positional arguments:
an argument has a postion. that is not a keyword argument. Positional arguments can appear at the *beginning* of an argument list and/or be passed as elements of an iterable preceded by *. For example:

```
complex(3, 5)
complex(*(3, 5))
```

2. keyword argument: an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by **. For exmaple:

```
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
```

rule:

- Arbitrary positional arguments ( *args )
- Arbitrary keyword arguments ( **kwargs )
- In Python2, you are not allowed to put keyword arugumnets before positional arguments.

So it has to be like below:

withPositionalArgs(3, ae=9,*(3, 5), **{'real': 3, 'imag': 5})

- The positional arguments must come first
- The keyword arguments
- then *args, (positional)
- then **kwargs (keyword)
- In Python3, the order has been relaxed. (For example, *args can come before a keyword argument in the function definition.)
ref: <https://stackoverflow.com/questions/12332195/using-default-arguments-before-positional-arguments> . e.g.

```
def withPositionalArgs(*args, ae=9):
```

## range([start], stop[, step])

1. Python for loop does NOT require an indexing variable(e.g. option 2) to set beforehand. so if need index, range() function will does the job (option 1):

 ```
 OPTION 1)
 b='Python'
 for idx in range(len(b)):
  print(idx, b[idx])
 0 P
 1 y
 2 t
 3 h
 4 o
 5 n
 ```

 above more like java style for loop with (int idx=0; idx < len(b); idx++)...
 VS.
 use build in to access element directly without index need

 ```
 OPTION 2)
 b = 'Python'
  for idx in b:
  print(idx)
 P
 y
 t
 h
 o
 n
 ```

2. range([start], stop[, step]) function returns a sequence of numbers.

- start:starting from 0 by default,
- step: increments by 1 (by default),
- stop: at a specified number.but not including this number.
 can use negtive number to reverse - look at Option 4) in String section below

## String

* Python String: list --> <https://www.programiz.com/python-programming/methods/string>

1. substring: [return string]

- string[start:end]: Get all characters from index start to end-1 (Note - exclude 'end')
- string[:end]: Get all characters from the beginning of the string to end-1
- string[start:]: Get all characters from index start to the end of the string
- string[start : end : step]: Get all characters from start to end-1 discounting every step character

   NOTE - substring wont change original string
   refer: <https://guide.freecodecamp.org/python/is-there-a-way-to-substring-a-string-in-python/>

2. assert: [return Boolean]

- .islower(), .isupper(), .isalpha(), .isalnum(), [.isdecimal() < .isdigit() < isnumeric() (containing decimal, digit)]
- .isspace(): Characters that are used for spacing are called whitespace characters. For example: tabs, spaces, newline etc. Return True if *all* characters (only whitespace)in the string are whitespace characters

3. search: [return index]

- .index(sub[, start[, end]]) & .find(sub[, start[, end]]) both return lowest index of matching substring takes 3 params. substring, start(optional), end (optional). except substring doesnt exist return -1 for find() vs. index return exceptions

  1. It's the substring to be searched in the str string.
  2. start and end (optional) - substring is searched within str[start:end]

- .rfind(sub[, start[, end]]) find the hight index of matching substring (from right most)
  usage example:

  ```
  # How to use find()
  if  (quote.find('be,') != -1):
    print("Contains substring 'be,'")
  else:
    print("Doesn't contain substring")

 ```

- .startswith(prefix[, start[, end]]) & .endswith(suffix[, start[, end]]): Return True/false to checksif String Starts/ends with the Specified String. params: start & end are optional
- .counts(sub[, start[, end]]): returns the number of occurrences of a substring in the given string.

4. replace: [return string]

- .replace(old, new [, count]):  returns a copy of the string where all occurrences of a substring is replaced with another substring.
    1. count (optional) - the number of times you want to replace the old substring with the new substring
    2. If count is not specified, replace() method replaces all occurrences of the old substring with the new substring.

5. remove: [return string]

- .strip([chars]): if char not provided, the method removes any whitespace from the beginning or the end; can pass character.
        if char is passed, it will search all the char of the set one by one form left and right side of the target string.
        If a char in the string s isn't in the set than *no further* checking is done form that side and stop from that side
        searching will be continue from the other side till similar thing is happen form that side.
        if char in string s is found in set than that char is removed and continue
        example:
        s="this is tricky"; s.strip("thsy") output: 'is is trick'
        1) make 'thsy' as char set - B [t,h,s,y]
        2) search char A by char from most-left and most left
  - if char A is in B, found and removed and continue
  - else chart A is not in B, not found and stop

- .lstrip([chars]): removes characters from the left based on the argument (a string specifying the set of characters to be removed).
- .rstrip([chars]): returns a copy of the string with trailing characters removed (based on the string argument passed).

6. split: [return a list]

- .split([separator [, maxsplit]]) : Splits String from Left

  1. Separator (optional)- The is a delimiter. The string splits at the specified separator. If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
  2. maxsplit (optional) - The maxsplit defines the maximum number of splits. The default value of maxsplit is -1, meaning, no limit on the number of splits.
     If maxsplit is specified, the list will have the maximum of maxsplit+1 items.
  
  ```

   >>> a = 'Milk, Chicken, Bread'
   >>> left=a.split[', ', 1](0)
   >>> right=a.split[', ', 1](1)
   >>> print(left)
   Milk
   >>> print(right)
   Chicken, Bread
   >>> print(left, right)
   Milk Chicken, Bread
   new string: Milk(as left) Chicken, Bread(as right)

  ```

- note: there's NO Left split as split as working as split from 'left'
- .rsplit([separator [, maxsplit]]): plits string from the Right, at the specified separator and returns a list of strings.
- .splitlines() : The splitlines() method splits the string at line breaks and returns a list of lines in the string.

7. slice: [return string] - not ONLY apply string, The slice object is used to slice a given *sequence* (string, bytes, tuple, list or range)
 start - starting integer where the slicing of the object starts
 stop - integer until which the slicing takes place. The slicing stops at index stop - 1. [if spacify, then it will be `stop` then `start']
         e.g.
   slice[stop] or
   slice[start, stop] or
   slice[start, stop, step]

 step - integer value which determines the increment between each index for slicing. using '-1' to become reverse, e.g. from right to left

 ```

 >>> b='Python'
 >>> slice(3)
 slice(None, 3, None)
 >>> type(slice(3))
 <class 'slice'>
 >>> x=slice(3)
 >>> b[x]
 'Pyt'
 >>> b='Python'
 >>> x=slice(1,5,2)
 >>> type(x)
 <class 'slice'>
 >>> b[x]
 'yh'
 >>> b='Python'
 >>> x = slice(-1, -4, -1)
 >>> b[x]
 'noh'

 ```

 use for reverse pring string:

 ```

 Option 1): using slice() - note: can use not only string but other collections like list and etc.
 >>> b='Python'
 >>> slice(-1,-1-len(b),-1)
 slice(-1, -7, -1)
 >>> x=slice(-1,-1-len(b),-1)
 >>> b[x]
 'nohtyP'

 Option 2): using `substring` to reverse
 >>> print(b[-1::-1])
 'nohtyP'

 Option 3): for loops using explicit idx (e.g. without range())
 >>> b='Python'
 >>> idx=0
 >>> a=''
 >>> for ch in b:
 ...     a+=b[-1-idx]  || a+=b[len(b)-1-idx]
 ...     idx=idx+1
 ...
 >>> print(a)
 nohtyP

 Option 4): for loops with range() (simpler than Option 2. note range 'end' not include the end indx)
 >>> b='Python'
 >>> a=''
 >>> for idx in range(-1, -1-len(b), -1):
 >>> a+=b[idx]
 >>> print (a)
 nohtyP

 ref: <https://www.programiz.com/python-programming/methods/built-in/slice>

5. convert:

- .lower(), .upper()...  

   refer: <https://www.w3schools.com/python/python_strings.asp>
    <https://www.programiz.com/python-programming/methods/string>
    <https://stackoverflow.com/questions/13783934/what-does-s-strip-do-exactly> [.strip()]

## List

methods modify original list:

1. Add item: list.append(x), list.insert(i, x). it can also be used to append a list: e.g. the list to append is consider to be one item. so it's better you start with empty list and add one sets at a time
2. Remove item:  list.remove(x) [only remove first matching item not all],   list.pop([i])
3. Order: sort(), reverse()
4. Clone: copy(). note: x=[a,b,c], x=y both x,y refer to the same list
5. Find/Search: index(sub[, start[, end]])
7. Count: .count(x)
6. use as:
 Stack:  [last-in, first-out]:  .append(x), .pop()
 Queues: [first-in, first-out]:  .append(x), .pop(0)

execise code: <https://github.com/kangli914/pycharm/blob/master/dummy/list_dummy.py>

## Read Write File

<https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python>

f = open("FILE", "r")

 Mode | Description
--- | ---
'r' | This is the default mode. It Opens file for reading.
'w' | This Mode Opens file for writing. If file does not exist, it creates a new file.If file exists it truncates the file.
'x' | Creates a new file. If file already exists, the operation fails.
'a' | Open file in append mode. If file does not exist, it creates a new file.
't' | This is the default mode. It opens in text mode.
'b' | This opens in binary mode.
'+' | This will open a file for reading and writing (updating)

read line by line:

1) directly working file object - Looping over a file object

```
file='readme.txt'
with open(file) as f_read:
      for line in f_read:
          # end='' will eliminate the newline feed in printout
          print(line, end='')
```

2) using readlines() which returns array of lines - Looping over readlines()

```
file='readme.txt'
with open(file) as f_read:
    # readlines() returns a 'list' type
    for line in f_read.readlines():
    print(line, end='')
```

both output: (each line is a string
a1
b2
c3

```

Read in file and write the content to another file

```

rfile='readme.txt'
wfile="writeout.txt"
with open(rfile, 'r', newline='') as f_read, open(wfile, 'w', newline='') as f_write:

# f_read.readlines() returned a list of lines

    for line in reversed(f_read.readlines()):
        f_write.write(line)
output:
c3
b2
a1

```

'''
There are two ways to turn A file into A `list` of lines
'''

```

with open(rfile) as f_reader:
    dataset = [line for line in f_reader]
    print("type of dataset:", type(dataset))
    print(dataset)

with open(rfile) as f_reader:
    # readlines() returns a 'list' type
    lines = f_reader.readlines()
    print('type of lines:', type(lines))
    print(lines)
    print("line 0:", lines[0])

```

'''
output: note that

1) each line is treated as string(*) - e.g. each row is a string
2) every line has the '\n' charactors

type of dataset: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
type of lines: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
'''

A shorter one line code:

```

lines = [line for line in open(rfile)]
print("one line code:", lines, 'one line type:', type(lines))

```

'''
output:
one line code: ['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n'] one line type: <class 'list'>
'''

'''
Below turn a Read in file into a 2 dim array '[[ ]]': a outter array of rows, and each row is another array of eliments in array separated by (,) comma.  
'''
Striping out the '\n' and turn a line into a List(*) by splitting by comma(,) as opposed to string e.g. each row now is a list of data not a string anymore

```

lines = [line.strip().split(',') for line in open(rfile)]
print("array of array - 2 dim array", lines, 'one line type:', type(lines))

```

'''
output:
array of array [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], ['6/28/2019', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'], ['6/29/2019', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']] one line type: <class 'list'>
'''
Looping through 2 dim arrays

```

for i in range(len(lines)):
    for j in range(len(lines[i])):
        print("element: [", lines[i][j], "] @ row {}, column {}".format(i, j))

```

Problem imposed when using *without* Python CSV module:

1) data like movie title with comma to split the titles, e.g. "The Good, the Bad"
2) although above code convert each row = a list of elements but all of elements type are still strings
Hence, using Python CSV module - NEXT

## Read Write CSV File

<https://www.youtube.com/watch?v=q5uM4VKywbA>
<https://realpython.com/python-csv/>

# Python CSV module

### CSV Reader

rfile='dummy_marketdata.csv'

note:

open file with newline='' keyword argument and passed in an empty string:
this is because depending on your system, strings may end with a new line carriage return or both,
this technique will ensure the csv module will work correctly across all platforms

```

file = open(rfile, 'r', newline='')
reader = csv.reader(file)

header = next(reader)
dataset = [row for row in reader]
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        print("dataset element: [", dataset[i][j], "] @ row {}, column {}".format(i, j))
file.close()

```

'''
output: - note by using csv.reader, it automatically convert to previously mentioned array of array - 2 dim array:
[['6/28/2019', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'], ['6/29/2019', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']]
'''

```

file = open(rfile, 'r', newline='')
reader = csv.reader(file)
date_set = [row[0].strip() for row in reader]
print("dateset with 1st column as date string:", date_set)
file.close()

```

'''
output:
dateset with 1st column as date string: ['Date', '6/28/2019', '6/29/2019']
'''

### CSV Reader with custom dialect defined

<https://realpython.com/python-csv/>

input:
 "AAA", "BBB", "Test, Test", "CCC"
 "111", "222, 333", "XXX", "YYY, ZZZ"

* If quoting is set to csv.QUOTE_MINIMAL, then .writerow() will quote fields only if they contain the delimiter or the quotechar. This is the default case.
* If quoting is set to csv.QUOTE_ALL, then .writerow() will quote all fields.
* If quoting is set to csv.QUOTE_NONNUMERIC, then .writerow() will quote all fields containing text data and convert all numeric fields to the float data type.
* If quoting is set to csv.QUOTE_NONE, then .writerow() will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.

```

csv.register_dialect(
    'custom_dialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\t\r\n',
    quoting = csv.QUOTE_MINIMAL
)

with open('readme.txt','r', newline='') as f:
  data = csv.DictReader(f, dialect=csv)
  for row in data:
        print("csv row:", row)

```

output:
 csv row: OrderedDict([('AAA', '111'), (' "BBB"', ' "222'), (' "Test', ' 333"'), (' Test"', ' "XXX"'), (' "CCC"', ' "YYY'), (None, [' ZZZ"'])])

```

with open('readme.txt','r', newline='') as f:
  data = csv.DictReader(f, dialect='custom_dialect')
  for row in data:
        print("custom dialect row:", row)

```

output:
 custom dialect row: OrderedDict([('AAA', '111'), ('BBB', '222, 333'), ('Test, Test', 'XXX'), ('CCC', 'YYY, ZZZ')])

### CSV Writer

```

file = open(rfile, 'r', newline='')
reader = csv.reader(file)

# The first line is the header

header = next(reader)

data = []
for row in reader:
    # row = [Date(datetime), Open(double), High(double), Low(double), Close(double), Volume(integer), Adj Close(double)]
    p_date = datetime.strptime(row[0], '%m/%d/%Y')
    p_open = float(row[1])
    p_high = float(row[2])
    p_low = float(row[3])
    p_close = float(row[4])
    p_volume = int(row[5])
    p_adj = float(row[6])
    data.append([p_date, p_open, p_high, p_low, p_close, p_volume, p_adj])

file2write = 'writout.csv'
with open(file2write, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["date", "return"])

    for i in range(len(data) - 1):
        today_row = data[i]
        yesterday_row = data[i+1]
        today_date = today_row[0]
        daily_return = today_row[-1] - yesterday_row[-1]
        writer.writerow([today_date, daily_return])

```

output:

date,return
2019-06-29 00:00:00,-4.700024000000099

### Using dialec

<https://realpython.com/python-csv/>

Using custom Dialect instead of defaulting 'excel'
<https://www.geeksforgeeks.org/working-csv-files-python/>

In csv modules, an optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV format.
By default, csv module uses excel dialect which makes them compatible with excel spreadsheets.
You can define your own dialect using register_dialect method.

input csv: to read
Note -

1) special char '|' will be double quoted  in output since our delimiter is '|'
2) there will be a 'tab' in the new line in output

Date,Open,High,Low,Close,Volume,Adj Close
6/29/2019,|576.11258,584.512631,576.002598,582.162619,1284100,582.162619
6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643

* delimiter: specifies the character used to separate each field. The default is the comma (',').

* quotechar: specifies the character used to surround fields that contain the delimiter character. The default is a double quote (' " ').
* escapechar: specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.

```

csv.register_dialect(
    'mydialect',
    delimiter = '|',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\t\r\n',
    quoting = csv.QUOTE_MINIMAL
)

with open('dummy_marketdata.csv', 'r', newline='') as fr, open('writout_2.csv', 'w', newline='') as fw:
    reader = csv.reader(fr)
    writer = csv.writer(fw, dialect='mydialect')

    header = next(reader)
    writer.writerow(header)

    rows = [line for line in reader]
    writer.writerows(rows)

```

output:

1) special char '|' will be double quoted  in output since our delimiter is '|'
2) there will be a 'tab' in the new line

Date|Open|High|Low|Close|Volume|Adj Close
6/29/2019|"|576.11258"|584.512631|576.002598|582.162619|1284100|582.162619
6/28/2019|585.002622|587.342658|584.002627|586.862643|978600|586.862643

### DictReader

Read and write data to/from CSV in dictionary form using the DictReader and DictWriter classes

```

with open('readme.txt','r', newline='') as f:
  data = csv.DictReader(f)
  for row in data:
        print(row)
        print(row['date joined'] + str(row.get(None)))

```

output of 'row': is an Ordered Dictionary:

 OrderedDict([('name', 'john smith'), ('address', '1132 Anywhere Lane Hoboken NJ'), ('date joined', ' 0730'), (None, ['Jan 4'])])

 0730['Jan 4']

 0816['March 2']

### DictWriter

```

with open('writeout_3.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

output:
    first_name,last_name
    Baked,Beans
    Lovely,Spam
    Wonderful,Spam

```

## File Path

import os

## OS.Path

input_dir = "Z:\\Workspaces\\GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33"
print(os.path.normpath(input_dir))
```Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33```

print(os.path.abspath(input_dir))
```Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33```

print(os.getcwd())
```C:\workspace\_github\pycharm\dummy```

Break file path by directory and file name:

There are 2 ways: (achieve the same goal)

1 - using os.path.split(FILE)

 ```

 file = "Z:\\Workspaces\\GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33.txt"
 filename, ext = os.path.split(dummyfile)
 print("filedir: ", filename, '\n', "filename:", ext)
 output:
 filedir:  Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results
 filename: N_2019-05-17_08-33.txt

 ```

2 - using os.path.dirname(FILE) & os.path.basename(FILE)

 ```

 file = "Z:\\Workspaces\\GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33.txt"
 print("filedir: ", os.path.dirname(file), '\n', "filename:", os.path.basename(file))
 output:
 filedir:  Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results
 filename: N_2019-05-17_08-33.txt

 ```

os.path.normpath(path)

Normalize a pathname by 1) collapsing redundant separators and up-level references so that A//B, A/B/, A/./B and A/foo/../B all become A/B.
2) On Windows, it converts forward(/ - linux) slashes to backward slashes (\ - windows)

```

file = "Z://Workspaces//GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33.txt"
print(os.path.normpath(file))
output:
Z:\Workspaces\GenericDataLake\apache-jmeter-4.0\results\N_2019-05-17_08-33.txt

```

os.path.normcase(path)

Normalize the case of a pathname. 1) On Windows, convert all characters in the pathname to lowercase, and 2) also convert forward slashes (/ - linux) to backward slashes (\ - windows)

```

file = "Z://Workspaces//GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33.txt"
print(os.path.normcase(file))
output:
z:\\workspaces\\genericdatalake\apache-jmeter-4.0\results\n_2019-05-17_08-33.txt

```

print[input_dir.rsplit("\", 1](1)])
```N_2019-05-17_08-33```

split file and extention: e.g. dummy && .txt

```

file = "dummy.txt"
root, ext = os.path.splitext(file)
print(root, ext)

in case file has long path:

dummyfile = "Z:\\Workspaces\\GenericDataLake\\apache-jmeter-4.0\\results\\N_2019-05-17_08-33.txt"
filename, ext = os.path.splitext(os.path.basename(dummyfile))
print("filename: ", filename, '\n', "file ext:", ext)
filename:  N_2019-05-17_08-33
file ext: .txt

```

to walkthrought a directory:

```

for root, dirs, files in os.walk("C:\\workspace\\_github"):
    for file in files:
        print("file name:", os.path.join(root, file))
    for dir in dirs:
        print("dir name:", os.path.join(root, dir))

```  

## Time

*time.time():*

```

print("time.time() in seconds:", time.time(), "type:", type(time.time()))
time.time() in seconds: 1560964870.9869883 type: <class 'float'>

```

*Representation betwen time (local, UTC) and epoch:*

1. time.gmtime([epoch_secs]): from 'seconds since the epoch' (if not specify time()) to 'struct_time in UTC'
2. time.localtime([epoch_secs]): from 'seconds since the epoch' (if not specify time()) to 'struct_time in local time'
3. time.calendar.timegm(t): from 'struct_time t in UTC' to 'seconds since the epoch' (inverse function of time.gmtime)
4. time.mktime(t): from 'struct_time t in local time' to 'seconds since the epoch' ( inverse function of localtime())

 ```

 Local time: Wed Jun 19 14:47:18 2019
 print("time.gmtime():", time.gmtime())
 print("time.localtime():", time.localtime())

 time.gmtime(): time.struct_time(tm_year=2019, tm_mon=6, tm_mday=19, tm_hour=18, tm_min=47, tm_sec=18, tm_wday=2, tm_yday=170, tm_isdst=0)
 time.localtime(): time.struct_time(tm_year=2019, tm_mon=6, tm_mday=19, tm_hour=14, tm_min=47, tm_sec=18, tm_wday=2, tm_yday=170, tm_isdst=1)

# once in 'struct_time' it access element by .tm_year

 print("time.gmtime().tm_year:", time.gmtime().tm_year)
 time.gmtime().tm_year: 2019
 <https://www.programiz.com/python-programming/time>

 ```

20190619T19:41:03-0500 = 1560973263

*time.asctime([t]):*

Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string

```

print(time.asctime(time.gmtime(1560973263)), type(time.asctime(time.gmtime(1560973263))))
print(time.asctime(time.localtime(1560973263)), type(time.asctime(time.localtime(1560973263))))
Wed Jun 19 19:41:03 2019 <class 'str'>
Wed Jun 19 15:41:03 2019 <class 'str'>

```

**Convrting time from epoch to str in both UTC and Local:**

1. use gmtime(epoch), localtime(epoch) to convert epoch to 'struct_time' object
2. then use ascttime(t) convert 'struct time' to string or use strftime(format[, t]) with specified format

or

Converting 'local' time only from epoch to str directly without going through 'struct_time' using 'time.ctime()' below:

*time.ctime(epoch_secs):*

Purpose was similar to 'time.localtime': epoch to time but 'str' directly instead of via 'struct_time'

```

print("time.ctime():", time.ctime(1560973263), "type:", type(time.ctime(1560973263)))
time.ctime(): Wed Jun 19 15:41:03 2019 type: <class 'str'>

```

*time.strftime(format[, t]):*

Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.

```

struct = time.gmtime(1560973263)
print(time.strftime("%Y%m%dT%H:%M:%S%z", struct))
20190619T19:41:03-0500

```

**Convrting time in str to epoch:**

1. use time.strptime(format[, t]) to parse string into 'struct_time' object
2. then use time.calendar.timegm(t) or time.mktime(t) to convert 'struct_time' to epoch

*time.strptime()*

parses a string representing time and returns struct_time.

```

time_string = "19:41:03,19 June, 2019"
struct = time.strptime(time_string, "%H:%M:%S,%d %B, %Y")
print(struct)
print(calendar.timegm(struct))  

time.struct_time(tm_year=2019, tm_mon=6, tm_mday=19, tm_hour=19, tm_min=41, tm_sec=3, tm_wday=2, tm_yday=170, tm_isdst=-1)
1560973263

```

Convert time in str to ISO string format using 'struct_time' as middle tir:


date_string='2019-05-17_08-33'
time_struct = time.strptime(date_string, '%Y-%m-%d_%H-%M')
print(time.strftime('%Y-%m-%dT%H:%M:%S%z', time_struct))
2019-05-17T08:33:00-0400
```

## Iterable, Iterator, Generator

### Concept

* quick good overview: <https://www.youtube.com/watch?v=BC77x_GLmxo&list=PL1A2CSdiySGLPTXm0cTxlGYbReGqTcGRA&index=5>
* <https://www.programiz.com/python-programming/iterator>
* <https://www.geeksforgeeks.org/python-difference-iterable-iterator/>
* Sequences (strings, lists, and tuples) are the most common form of iterables,

1 Iterable:

- Iterable vs Iterator:

  Iterable is an object which one can iterate over. An iterable object can be put inside a for loop or list comprehension.

  Iterator is an object which is used to iterate over an iterable object

- An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple, string, file and etc. are iterables.
- The iter() function (which in turn calls the ____iter__()__ method) returns an iterator from them.

2 Iterator:

- Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

- Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol. The iter() function (which in turn calls the____iter__()__ method) returns an iterator from them.

- Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, __generators__ etc. but are hidden in plain sight.

3 Generator:

- Generator is an Iterator. A generator is built by calling a function that has one or more __yield__ expressions

- Generator are ordinary functions defined using yield instead of return. When called, a generator function returns a __generator__ object, which is a kind of __iterator__ - it has a next() method. When you call next(), the next value yielded by the generator function is

- Gnerator is another way of creating iterators. __It uses a function rather than a separate class__

- Generates the backgroup code for the iter() and next() methods

- Uses a special statement called yeild which saves the state of the generator and set a resume point for when next() is called again.

- Generator vs Return:

  Like the return statement, the yield statement commands the function to send back a value to the caller

  Unlike  the resturn statement, the yeild statement does nto actually terminate teh functions's exedcution.  Rather, execution is termporatily halted until the generator is resumed by the caller, at which point it pick4es up where it left off

- Memory efficient:
  
  A genertor fucntion doesn't execute right away. instead it executes until it is told to yield a value, and then it continues execution until told to do so again

  Generators may represent infinite sequences. there is no explicit requirement that a generator terminate at all.

  It is simply the responsibility of the code iterating over the generators to break out of the sequence when appropriate(e.g. break statement)

  **test commit
  ** test commit2
  ** test commit3

## Decorators

### Concept

#### First-Class Function

<https://www.youtube.com/watch?v=kr0mpwqttM0>

__function__ in python is treated as first-class citizens called first class object or called first class function. A first-class citizen in a programming language is an entity which supports all the operations generally available to other entities. these operations typically includes

basically, First-class fucntion allows us to treat function as objects.

- assign function to a variable
- pass function as the arguments
- return the fucntion as the result of other functions

exmaples:

- assign function to a variable:

```
""" here it treats varaible f as square() function so we can use f as if using square()
def square(x):
  return x * x

f = square

print (f(5))

```

- passing a function (e.g. square() ) as arguments:

```

def square(x):
    return x * x


def new_container(func, list):
    """take function as arguments"""
    new_list = []
    for item in list:
        new_list.append(func(item))
    return new_list

new_square = new_container(square, [1, 2, 3, 4])
print(new_square)

## output: [1, 4, 9, 16]
```

- return the fucntion as the result of other functions

Note:

return log_message is no `()` so it wont get executed when it was defined

here it is important to think log_hi() is a function and whenever it refers log_hi function it is same as = log_message() of the innner function  and because log_message() in the inner function doesn't take any argument so as log_hi()

when calling line log_hi w/o `()` the function will not executed

return the __same__ name of the functions

```
def logger(msg):

  def log_message():
    print('Log:', msg)

    return log_message

log_hi = logger("Hi")
log_hi()

```

#### High-Order Function

A function accepts other fucntions as arguments or returns fucntions as the result of other functions.

This concept related to the 3rd point in Python First-Class fucnction: e.g. return the fucntion as the result of other functions

#### Closure

<https://www.youtube.com/watch?v=swU3c34d2NQ&t=5s>

Closure is an inner function that remembers and has access to variables(e.g. call free variables) in the local scope in which it was created.
even after the outer fucntion has finished executing.

CLosure allows us to take advantage of first-class functions, and return an inner function that remembers and has access to variables local to the scope in which they were created(e.g. usually from out_function that was passed in)

for example:

the inner fucntion log_hi() still remembers and has access to the msg variables when logger was created even after the outer fucntion log_hi = logger("Hi") has finished executing @ line `log_hi = logger("Hi")` which really just mke log_hi eqaul to log_message w/o really executing.

<https://www.youtube.com/watch?v=swU3c34d2NQ>

#### Decorators works togehter with High-order function & closure

#### Decorators Concept

<https://www.youtube.com/watch?v=FsAPt_9Bf3U>

A decorator is just a function that takes another function as an argument, adds some kind of functionality, and then returns another function. All of this is without altering the source code of the original function that you passed in.

The idea here is that we have a __high-order fucntion x__ which takes a function y and it (e.g. funciton x) performs some operations before calling that function y.

and then you take this modified function x (e.g. think of a pathced one on top of function y), and you save it __as the same name as__ the original function.

when you call the original fucntion eseentially, you are calling this patched version of the function (since it's the __same name__)

__Terms__:

Patching function: is esentially decorating fucntion.

Function annotation: taking a function and you are annotating it so that it's modified at __runtime__ through some dynamic behavior.

```
def quicker_fibonacci(func):
    """
    high order function version of fibonacci:
    if it's in cache, return cached value,
    else not in cache, then call original fib for calcs value
    """

    cached = {}

    def wrapper(n):
        if n not in cached:
            cached[n] = func(n)

        return cached[n]

    return wrapper

@quicker_fibonacci
def fib(n):
    """basic fibonacci version - most inefficient"""
    if n <= 1:
        return n

    else:
        return fib(n-2) + fib(n-1)

fib(40)  # same as fib = quicker_fibonacci(fib) then fib(40)
```

note - when you call the original fucntion eseentially, you are calling this patched version of the function (since it's the __same name__)

```
fib(40)  # same as fib = quicker_fibonacci(fib) then fib(40)
```

## Context Manager

### Concept

THe context manager idea is to create a ___context___ that requires some setup before starting and some cleanup at the end.

Context Manager uses _Decorators_, _Generator_  concepts together (e.g. relationship - see timer_decorator_cibtext-manger.py)
