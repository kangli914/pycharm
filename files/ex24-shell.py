#!/usr/bin/env python3

"""Output users in /etc/pawd using the same shell."""

import csv
import sys
from collections import defaultdict


def open_file_safe(file, mode="r"):
    """Open file safe."""

    try:
        return open(file, mode=mode, newline="")
    except OSError:
        sys.exit(f"error in opening the file {file}")


if __name__ == "__main__":
    rfile = "/etc/passwd"
    wfile = "ex24-shell.out"
    shell_dict = defaultdict(list)

    with open_file_safe(rfile) as f_reader, open_file_safe(wfile, mode="w") as f_writer:
        reader = csv.reader(f_reader, dialect="unix", delimiter=":")
        for row in reader:
            # print(row)
            # print(type(row))
            # row is a list
            # ['nvidia-persistenced', 'x', '126', '133', 'NVIDIA Persistence Daemon,,,', '/nonexistent', '/usr/sbin/nologin']
            # <class 'list'>
            # print(', '.join(row))
            if not row[0].strip().startswith(("#", "\n")):
                shell_dict[row[-1]].append(row[0])

    for k, v in shell_dict.items():
        # ', '.join(row) join a list of iterable like list/tuple/dictionary and return a string
        # https://www.codingem.com/python-join-list-of-strings/
        print(f"{k}: {', '.join(v)}")
