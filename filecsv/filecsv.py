import csv
# import datetime class from datetime module
from datetime import datetime
### Reading file:

'''
read line by line. There are two ways to do that:
'''

# 1) directly working file object - Looping over a file object
# rfile='readme.txt'
rfile='dummy_marketdata.csv'
with open(rfile, newline='') as f_read:
    for line in f_read:
        # end='' will eliminate the newline feed in printout
        print(line, end='')

# 2) using readlines() which returns array of lines - Looping over readlines()
with open(rfile, newline='') as f_read:
    # readlines() returns a 'list' type
    for line in f_read.readlines():
	    print(line, end='')
'''
# output:
Date,Open,High,Low,Close,Volume,Adj Close
6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643
6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619
'''
###############################################################################

'''
There are two ways to turn A file into A `list` of lines
'''
with open(rfile, newline='') as f_reader:
    dataset = [line for line in f_reader]
    print("type of dataset:", type(dataset))
    print(dataset)

with open(rfile) as f_reader:
    # readlines() returns a 'list' type
    lines = f_reader.readlines()
    print('type of lines:', type(lines))
    print(lines)
    print("line 0:", lines[0])

'''
# output: note that
1) each line is treated as string(*) - e.g. each row is a string
2) every line has the '\n' charactors
 
type of dataset: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
type of lines: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
'''

# a shorter one line code: each row is a string
lines = [line for line in open(rfile, newline='')]
print("one line code:", lines, 'one line type:', type(lines))
'''
output:
one line code: ['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n'] one line type: <class 'list'>
'''
# striping out the '\n' and turn a line into a List(*) by splitting by comma(,) as opposed to string e.g. each row now is a list of data not a string anymore
lines = [line.strip().split(',') for line in open(rfile, newline='')]
print("array of array - 2 dim array:", lines, 'one line type:', type(lines))
'''
output:
array of array:
[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], ['6/28/2019', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'], ['6/29/2019', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']] one line type: <class 'list'>
'''

for i in range(len(lines)):
    for j in range(len(lines[i])):
        print("element: [", lines[i][j], "] @ row {}, column {}".format(i, j))




###############################################################################

rfile='readme.txt'
wfile="writeout_tmp.txt"
with open(rfile, 'r', newline='') as f_read, open(wfile, 'w', newline='') as f_write:
    for line in reversed(f_read.readlines()):
        f_write.write(line)

rfile='readme.txt'
wfile="writeout.txt"
with open(rfile, newline='') as f_read, open(wfile, 'w') as f_write:
        csvreader = csv.reader(f_read, delimiter=',', quotechar='"')
        for row in csvreader:
            print(row)

###############################################################################

# Python CSV module:

rfile='dummy_marketdata.csv'
# note: open file with newline='' keyword argument and passed in an empty string:
# this is because depending on your system, strings may end with a new line carriage return or both,
# this technique will ensure the csv module will work correctly across all platforms
file = open(rfile, 'r', newline='')
reader = csv.reader(file)

header = next(reader)
dataset = [row for row in reader]
for i in range(len(dataset)):
    for j in range(len(dataset[i])):
        print("dataset element: [", dataset[i][j], "] @ row {}, column {}".format(i, j))
file.close()
'''
output: - note by using csv.reader, it automatically convert to previously mentioned array of array - 2 dim array:
[['6/28/2019', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'], ['6/29/2019', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']]
'''
file = open(rfile, 'r', newline='')
reader = csv.reader(file)
date_set = [row[0].strip() for row in reader]
print("dateset with 1st column as date string:", date_set)
file.close()
'''
output:
dateset with 1st column as date string: ['Date', '6/28/2019', '6/29/2019']
'''

###############################################################################
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

###
# using custom Dialect instead of defaulting 'excel'
# https://www.geeksforgeeks.org/working-csv-files-python/
'''
In csv modules, an optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV format. 
By default, csv module uses excel dialect which makes them compatible with excel spreadsheets. 
You can define your own dialect using register_dialect method.
'''
###

'''
input csv: to read 
Note -
1) special char '|' will be double quoted  in output since our delimiter is '|'
2) there will be a 'tab' in the new line in output

Date,Open,High,Low,Close,Volume,Adj Close
6/29/2019,|576.11258,584.512631,576.002598,582.162619,1284100,582.162619
6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643
'''

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

'''
output:
1) special char '|' will be double quoted  in output since our delimiter is '|'
2) there will be a 'tab' in the new line

Date|Open|High|Low|Close|Volume|Adj Close	
6/29/2019|"|576.11258"|584.512631|576.002598|582.162619|1284100|582.162619	
6/28/2019|585.002622|587.342658|584.002627|586.862643|978600|586.862643	
'''

