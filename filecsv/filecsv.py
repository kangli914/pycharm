### Reading file:

'''
read line by line. There are two ways to do that:
'''

# 1) directly working file object - Looping over a file object
# rfile='readme.txt'
rfile='dummy_marketdata.csv'
with open(rfile) as f_read:
    for line in f_read:
        # end='' will eliminate the newline feed in printout
        print(line, end='')

# 2) using readlines() which returns array of lines - Looping over readlines()
with open(rfile) as f_read:
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

'''
# output: note that
1) each line is treated as string(*) - e.g. each row is a string
2) every line has the '\n' charactors
 
type of dataset: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
type of lines: <class 'list'>
['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n']
'''

# a shorter one line code:
lines = [line for line in open(rfile)]
print("one line code:", lines, 'one line type:', type(lines))
'''
output:
one line code: ['Date,Open,High,Low,Close,Volume,Adj Close\n', '6/28/2019,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n', '6/29/2019,576.11258,584.512631,576.002598,582.162619,1284100,582.162619\n'] one line type: <class 'list'>
'''
# striping out the '\n' and turn a line into a List(*) by splitting by comma(,) as opposed to string e.g. each row now is a list of data not a string anymore
lines = [line.strip().split(',') for line in open(rfile)]
print("array of array - 2 dim array", lines, 'one line type:', type(lines))
'''
output:
array of array [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], ['6/28/2019', '585.002622', '587.342658', '584.002627', '586.862643', '978600', '586.862643'], ['6/29/2019', '576.11258', '584.512631', '576.002598', '582.162619', '1284100', '582.162619']] one line type: <class 'list'>
'''

for i in range(len(lines)):
    for j in range(len(lines[i])):
        print("element: [", lines[i][j], "] @ row {}, column {}".format(i, j))




###############################################################################



# rfile='readme.txt'
# wfile="writeout.txt"
# with open(rfile) as f_read, open(wfile, 'w') as f_write:
#     for line in reversed(f_read.readlines()):
#         f_write.write(line)
#
# rfile='readme.txt'
# wfile="writeout.txt"
# with open(rfile) as f_read, open(wfile, 'w') as f_write:
#         csvreader = csv.reader(f_read, delimiter=',', quotechar='"')
#         for row in csvreader:
#             print(row)
