#!/usr/bin/env python3

"""Sum tow columns container a number and ignore any line does not contain two numeric columns."""

import os
from pathlib import Path
import sys


def open_file_safe(file):
    try:
        return open(file)
    except OSError:
        sys.exit(f"having problem openning the file {file}!")


if __name__ == "__main__":
    # cwd_path = os.getcwd()
    # print(__file__ + "\n")
    dir_path = Path.cwd()
    file = dir_path / "ex18_2-cols-numbers.txt"

    total_sum = 0
    with open_file_safe(file) as f:
        for line in f:
                cols = line.strip().split('\t')  # split the line into two columns
                if len(cols) != 2:  # ignore any line that doesn't have two columns
                    continue
                try:
                    num1 = float(cols[0])  # convert the first column to a float
                    num2 = float(cols[1])  # convert the second column to a float
                except ValueError:
                    continue  # ignore any line that doesn't contain two numeric columns
                total_sum += num1 * num2  # multiply the two numbers and add the result to the total sum

    print(total_sum)
