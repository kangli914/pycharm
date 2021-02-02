#!/user/bin/env python3

"""Free playground.

Nothing needed to be commited
"""

from pprint import pprint
from collections import defaultdict

s = [("yellow", 1), ("blue", 2), ("yellow", 1), ("blue", 4), ("red", 1)]

# use dictionary with bare bone
d1 = {}
for k, v in s:
    item = d1.get(k)

    if not item:
    # d1[key] is the only way to change the value of dictionary given by the key
        d1[k] = item = []

    item.append(v)


# use setdefault
d2 = {}
for k, v in s:
    # only if k not exist for the first time it will insert key and value as empty list
    item = d2.setdefault(k, [])

    # if key exist, previous statement will return the list containing the item and then you continue performing appending
    item.append(v)


# use defaultdict
d3 = defaultdict(list)
# When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the 
# default_factory function which returns an empty list
# The list.append() operation then attaches the value to the new list.
# When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation 
# adds another value to the list.
for k, v in s:
    d3[k].append(v)


# use Set {e.g. like dictionary unique key w/o vlaue} and defaultdict to elimite the duplicates 
d4 = defaultdict(set)

for k, v in s:
    d4[k].add(v)


pprint(d1.items())
pprint(d2.items())
pprint(d3.items())
pprint(d4.items())
