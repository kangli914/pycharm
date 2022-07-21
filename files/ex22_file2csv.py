#!/usr/bin/env python3

"""Read a CSV file and write to a file.

It takes two filenames as arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
"""


import csv
import sys

import pandas


def open_file_safely(file, MODE="r"):
    """Open the file safely.

    Accep a filename as an argument and exits if having the issue."""
    # alway better include newline='' when reading csv
    # If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correc
    # https://docs.python.org/3/library/csv.html
    try:
        return open(file, MODE, newline='')
    except OSError:
        sys.exit(f"Error encountered when opening the file {file}!")


# use csv.reader
def passwd_to_csv_1(rfile, wfile):
    """read rfile as a passwd style file and write the output to wfile with TAB separted."""
    with open_file_safely(rfile) as f_reader, open_file_safely(wfile, MODE="w") as f_writer:
        reader = csv.reader(f_reader, dialect="unix", delimiter=":")
        # 'Dialect.quoting' and 'Dialect.quotechar' are mostly good for write out csv data.
        #  For example, the following will quote all the write out data with single quote instead of double quote when writing to the file and the default for Dialect.quoting is defaults to QUOTE_MINIMAL.
        # more rules here https://realpython.com/python-csv/
        writer = csv.writer(f_writer, dialect="unix", delimiter="\t", quoting=csv.QUOTE_ALL, quotechar="'")

        try:
            # Each row read from the csv file is returned as a list of strings
            for row in reader:
                # row are list/sequence, so use .join() to turn : into , seperated
                # print(f'Column are: {", ".join(row)}')

                # reader can have line_num() instead of using the inedex
                # print(reader.line_num)

                if not row[0].strip().startswith(("#", "\n")):
                    writer.writerow((row[0], row[2]))
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(rfile, reader.line_num, e))


# use csv.DictReader
def passwd_to_csv_2(rfile, wfile):
    """read rfile as a passwd style file and write the output to wfile with TAB separted."""
    with open_file_safely(rfile) as f_reader, open_file_safely(wfile, MODE="w") as f_writer:

        # The fieldnames parameter is a sequence. If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames.
        # here we give the first 3 column a name
        reader = csv.DictReader(f_reader, fieldnames=["name", "x", "user"], dialect="unix", delimiter=":")

        # Unlike reader, the fieldnames parameter of the DictWriter class is not optional!
        fieldnames = ["user_name", "user_id"]
        writer = csv.DictWriter(f_writer, fieldnames=fieldnames, dialect="unix", delimiter=",", quoting=csv.QUOTE_NONE, quotechar="'")

        # write csv header
        writer.writeheader()

        try:
            for row in reader:
                # startwith() can take tuples so here we skip the comments and blank lines
                if not row["name"].strip().startswith(("#", "\n")):
                    # note csv.DictWriter takes in a dictionary to write
                    writer.writerow({"user_name": row["name"], "user_id": row["user"]})
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(rfile, reader.line_num, e))


# use pandas
# https://realpython.com/python-csv/
def passwd_to_csv_3(rfile, wfile):
    # header=0 tells pandas to ignore the existing column
    df = pandas.read_csv(rfile,
                         sep=":",
                         index_col="name",
                         names=["name", "x", "user_id", "others_1", "others_2", "others_3", "others_4"],
                         header=0)
    # print(df)

    # In any case we should not provide indexed column (e.g. name) to the write_columns,
    # it would result key error

    # index=False will not write any column index 'name'
    write_columns = ["user_id"]
    df.to_csv(wfile, index=False, columns=write_columns, sep=",")

    # index=True (Default) will write the column index 'name'
    write_columns = ["user_id"]
    df.to_csv(wfile, index=True, index_label="new name", columns=write_columns, sep=",")

    '''
    # index=False
    user_id
    1
    2

    # index=True
    new name,user_id
    daemon,1
    bin,2
    sys,3
    '''


if __name__ == "__main__":
    passwd_to_csv_3("/etc/passwd", "dummy.txt")
