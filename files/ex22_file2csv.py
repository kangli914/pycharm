#!/usr/bin/env python3

"""Read a CSV file and write to a file.

It takes two filenames as arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
"""


import sys
import csv


def open_file_safely(file, MODE="r"):
    """Open the file safely.

    Accep a filename as an argument and exits if having the issue."""
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
        #  For example, the following will quote all the write out data with ? instead of double quote when writing to the file and the default for Dialect.quoting is defaults to QUOTE_MINIMAL.
        writer = csv.writer(f_writer, dialect="unix", delimiter="\t", quoting=csv.QUOTE_NONNUMERIC, quotechar="?")

        # Each row read from the csv file is returned as a list of strings
        for row in reader:
            # row are list/sequence, so use .join() to turn : into , seperated
            # print(f'Column are: {", ".join(row)}')

            if not row[0].strip().startswith(("#", "\n")):
            # if not row.startswith(("#", "\n")):
                writer.writerow((row[0], row[2]))


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


if __name__ == "__main__":
    passwd_to_csv_2("/etc/passwd", "dummy.txt")
