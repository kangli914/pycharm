#!/usr/bin/eny python3

"""Read apache log file and find what response codes were returned to users."""

import os

response_codes = set()
path = os.getcwd()

with open(f"{path}/dicts/apache.log", "r") as f:
    for line in f.readlines():
        resp_code = line.strip().split()[8]
        response_codes.add(resp_code)

print(response_codes)
