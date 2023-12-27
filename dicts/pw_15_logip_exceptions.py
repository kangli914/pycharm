#!/usr/bin/env python3

"""Open a log file from a Unix/Linux system—for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request’s success or failure), store a list of IP addresses that generated
that code."""


import os
from pathlib import Path


def open_file_safe(file, file_mode="r"):
    """Open file safe."""
    try:
        return open(file, mode=file_mode)
    except OSError:
        os.error("Error in open file {file}.")


def output_log(input_file):
    file_dict = dict()
    with open_file_safe(input_file) as f:
        for line in f:
            line = line.strip().split(" ")
            ip = line[0]
            code = line[8]
            try:
                ip_list = file_dict[code]
            except KeyError:
                print(f"{code} not exist. Creating an empty list")
                file_dict[code] = []
                file_dict[code].append(ip)
            else:
                ip_list.append(ip)

    return file_dict


if __name__ == "__main__":
    dir = Path.cwd()
    input_file = dir / "dicts" / "apache.log"
    result = output_log(input_file)
    for k, v in result.items():
        print(f"code: {k}, ips: {v}")
