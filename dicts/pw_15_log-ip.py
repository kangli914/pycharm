#!/usr/bin/env python3

"""Process apatch log file.

For each response code, store a list of IP addresses that generated that code
"""

import os
from collections import defaultdict

file = "apache.log"
cwd = os.getcwd()

with open(f"{cwd}/dicts/{file}") as f_reader:
    resp_lookup_list = defaultdict(list)
    # use set to eliminate the duplicates ips which genererated the same resposne code 
    resp_lookup_set = defaultdict(set)

    for line in f_reader:
        # print(line, end="")
        status = line.strip().split()[8]
        ip = line.strip().split()[0]

        # append to a List dictionary
        resp_lookup_list[status].append(ip)
        # append to a Set dictionary
        resp_lookup_set[status].add(ip)

for k, v in resp_lookup_list.items():
    print(k, v)
'''
200 ['111.222.333.111', '111.222.333.111', '111.222.333.115']
404 ['111.222.333.113']
504 ['111.222.333.124']
'''

print()
# use set to automaically elimite the duplicates
for k, v in resp_lookup_set.items():
    print(k, v)
'''
200 {'111.222.333.111', '111.222.333.115'}
404 {'111.222.333.113'}
504 {'111.222.333.124'}
'''
