#!/usr/bin/env python3

"""Read a CSV file and write given list of integer to column, to a file.

It takes two filenames as arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
"""

import csv
import sys


def open_file_saftly(file, MODE="r"):
    """Open the file safely.

    Accept a filename as an argument and exits if having the issue."""
    try:
        return open(file, MODE, newline="")
    except OSError as e:
        sys.exit(f"Error encountered when opening the file {file}: {e}!")

def passwd_to_csv_dict(rfile, wfile, col_list):
    """read rfile as a passwd style file and write the output to wfile with TAB separted."""
    with open_file_saftly(rfile) as f_reader, open_file_saftly(wfile, MODE="w") as f_writer:

        reader = csv.reader(f_reader, dialect="unix", delimiter=":")
        writer = csv.writer(f_writer,
                            dialect="unix",
                            delimiter="\t",
                            quoting=csv.QUOTE_ALL,
                            quotechar="'")
        try:
            # for row in reader:
            #     for col in col_list:
            #          if col < len(row):
            #             if not row[0].strip().startswith(("#", "\n")):
            #                 writer.writerow(col)

            for row in reader:
                if not row[0].strip().startswith(("#", "\n")):
                    select_items = [item
                                    for index, item in enumerate(row)
                                    if str(index) in col_list]
                    print(select_items)
                    writer.writerows(select_items)

        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(rfile, reader.line_num, e))


if __name__ == "__main__":
    # asking the user to enter a space-separated list of integers indicating which fields
    # should be written to the output CSV file
    print("Please enter space separted integer: ")
    cols = input().split(" ")
    passwd_to_csv_dict("/etc/passwd", "dummy2.txt", cols)
