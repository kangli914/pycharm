
import os

"use generator, exception handle togther wiht list unpacking"

def all_rows(file):
    try:
        with open(file, "r") as f:
            for line in f:
                yield line
    except FileNotFoundError as e:
        print(f"Error: can not of file with error {e}")

generator = all_rows("dummy_marketdata.csv")
header, *rows = generator
print(header, end="")
print(len(rows), end="")

# print(next(generator), end="")
# print(next(generator), end="")
