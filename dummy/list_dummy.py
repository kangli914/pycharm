'''
    List is a collection which is ordered and changeable. Allows **duplicate** members. []
    * ordered
    * changeable
    * allow duplicate
    good refernce: https://docs.python.org/3/tutorial/datastructures.html
'''

'''
list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
'''


thislist = ["apple", "banana", "cherry"]
thislist1 = ["apple", "pear", "cherry"]
thislist[1] = "orage"
print(thislist)

# for loop a list with idx
i=0
for item in thislist:
    print("my item:", item, "variable i:", i)
    print(thislist[i:])
    i = i + 1

# for loop a string
str="abcde"
idx=0
for ch in str:
    print(ch)
    print('access by index:', idx, 'with char', str[idx])
    idx = idx + 1



list_a = ["apple", "banana", "cherry"]

# append at the end
list_a.append("grap")
### [outcome]:  ["apple", "banana", "cherry", "grap"]

# insert at left/begin
list_a.insert(0, "orange")
# insert at right/end. same as append
list_a.insert(len(list_a), "orange")
### [outcome]:  ['orange', 'apple', 'banana', 'cherry', 'grap', 'orange']
print("List: list_a - ", list_a)

# remove from right/end using pop()
''' all 3 below are the same'''
#list_a.pop()
#list_a.pop(-1)
list_a.pop(len(list_a)-1)
# remove from left/begin
list_a.pop(0)
print("List: list_a after pop from right ", list_a)
### [outcome]:  ['apple', 'banana', 'cherry', 'grap']
# remove by item using remove()
list_a = ["apple", "banana", "cherry", "apple"]
list_a.remove("apple")
print(list_a)
### [outcome]:  ['banana', 'cherry', 'apple']

# sort
list_a = ["cherry", "apple", "banana"]
list_a.sort()
print("after sort:", list_a)
### [outcome]:  after sort: ['apple', 'banana', 'cherry']

# reverse
list_a.reverse()
print("after reverse:", list_a)
### [outcome]:  after reverse: ['cherry', 'banana', 'apple']

# copy
list_a = ["apple", "banana", "cherry"]
list_b = list_a.copy()
print("copy list:", list_b)


# index (note: 'end' will be excluded only search from index 'start' to index 'end-1')
# access by index(x[, start[, end]]). returns the position at the first occurrence of the specified item x
# same as 'string' index(sub[, start[, end]]) or find(sub[, start[, end]])
#print("index returned:", list_b.index("cherry", 0, 2))
### [outcome]:  ValueError: 'cherry' is not in list
print("index returned:", list_b.index("cherry", 0, 3))
### [outcome]:  index returned: 2

# slice/dice list like string but do not change the original list like above
list_a = ["apple", "banana", "cherry"]
# 1) like string (using substring) but do not change the original list like above
print(list_a[1:2:1])
### [outcome]:  ['banana']  (still a List)

## 2) using slice() to reverse the string (same as reverse())
a = "abc"
s = slice(-1, -1-len(list_a), -1)
#print(a[s])
print(list_a[s])


# use as stack [last-in, first-out]
stack = [1, 2, 3]
#stack.insert(len(stack), 4)
stack.append(4)
print(stack)
### [outcome]: [1, 2, 3, 4]
#stack.pop()
stack.pop(-1)
print(stack)
### [outcome]: [1, 2, 3]


# use as queue [first-in, first-out]
# look for 5.1.2. 'queue' for more efficient way to do so https://docs.python.org/3/tutorial/datastructures.html
queue = [1, 2, 3]
queue.append(4)
queue.pop(0)
print(queue)
### [outcome]: [2, 3, 4]


# find the difference of two lists
list_a = ["apple", "banana", "cherry"]
list_b = ["apple", "pear", "cherry"]
list_diff = []
def find_diffitems():
    for a in list_a:
        if a in list_b:
            print("found item: {} from list: {} in list {}".format(a, "A", "B"))
        else:
            list_diff.append(a)

    for b in list_b:
        if b in list_a:
            print("found item: {} from list: {} in list {}".format(b, "B", "A"))
        else:
            list_diff.append(b)

    return list_diff
print(find_diffitems())

list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_diff = []
def find_diffitems1():
    for a in list_a:
        for b in list_b:
            if b is not a:
                list_diff.append(b)
    return list_diff

print(find_diffitems1())

