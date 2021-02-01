#!/user/bin/env python3

"""Free playground.

Nothing needed to be commited
"""

from pprint import pprint
from collections import defaultdict

s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]

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
    # only if k not exist for the first it will set as list
    item = d2.setdefault(k, [])

    # if key exist, previous statement will return item as a list
    item.append(v)

# use defaultdict
d3 = defaultdict(list)
for k, v in s:
    d3[k].append(v)


pprint(d1)
pprint(d2)
pprint(d3)
