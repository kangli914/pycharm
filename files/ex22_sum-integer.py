#!/usr/bin/env python3

"""Sum and mean of the number on each line.

Create a CSV file, in which each line contains random integers between 10 and 100. Now read the file back, and print the sum and mean of the numbers on each line.
"""

import csv
import sys


def open_file_safely(file, MODE="r"):
    """Open the file safely.

    Accept a filename as an arugment and exits if haivng the issue."""
    # alway better include newline='' when reading csv
    # If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correct
    # https://docs.python.org/3/library/csv.html
    try:
        return open(file, MODE, newline="")
    except OSError:
        sys.exit(f"Error encountered when opening the file {file}!")


def find_avg_and_sum(rfile):
    """Find the average and sume of each line of the integers."""

    with open_file_safely(rfile) as f_reader:
        # here the default csv.QUOTE_MINIMAL won't work as all the read-in file containing only the integether
        # using csv.QUOTE_MINIMAL will add quote around the integer becoming to string where we can not perform
        # math ops
        # reader = csv.reader(f_reader, dialect="unix", delimiter=" ", quoting=csv.QUOTE_MINIMAL)
        # output: ['2', '2', '2']

        reader = csv.reader(f_reader, dialect="unix", delimiter=" ", quoting=csv.QUOTE_NONNUMERIC)
        try:
            # field for row in reader for field in row
            for row in reader:
                # print(row)
                print(f"line #{reader.line_num}, {sum(row)}, {sum(row)/len(row)}")
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(rfile, reader.line_num, e))


if __name__ == "__main__":
    find_avg_and_sum("files/ex22_input.txt")
