#!/usr/bin/env python3

"""This is a function that writes a dict to a CSV file.

Each line in the CSV file should contain three fields: (1) the key, which we will assume to be a string, (2) the value,
and (3) the type of the value (str or int).
"""

import csv
import sys


def open_file_safely(file, MODE="r"):
    """Open the file safely.

    Accept a file name as an argemetn and exits if having the issue."""
    try:
        return open(file, MODE, newline="")
    except OSError as e:
        sys.exit(f"Error encounter when opening the file {file}: {e}!")


def dict_to_csv(data, file):
    """convert a dictionary to a csv file.

    It uses csv.DictReader."""
    feild_names = ["key", "value", "type"]

    with open_file_safely(file, MODE="w") as f_writer:
        writer = csv.DictWriter(f_writer, fieldnames=feild_names, dialect="unix", delimiter=":", quoting=csv.QUOTE_NONE, quotechar=",")
        writer.writeheader()

        for k, v in data.items():
            try:
                writer.writerow({"key": k, "value": v, "type": type(v)})
            except csv.Error as e:
                sys.exit(f"Error encountered when writing the file {e}!")


if __name__ == "__main__":
    data = {"key1": "first", "key2": 2, "key3": "third"}
    dict_to_csv(data, "dummy.txt")
