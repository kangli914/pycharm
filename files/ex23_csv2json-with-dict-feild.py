#!/usr/bin/env python3

"""convert /etc/passwd from CSV to JSON file.
The JSON file will contain the equivalent of a list of Python dict.
This will require identifying each field with a unique column or key name
"""

import json
import os
import pathlib
from collections import defaultdict


def open_file_safely(file, mode="r"):
    """Open file safely and return the file wrapper when no error."""

    try:
        return open(file, mode)
    except OSError:
        os.error("Error encountered when openning the file {file}!")


if __name__ == "__main__":
    root = pathlib.Path("files")
    input_file = root / "ex18_faked_pd.txt"

    key_item = ["star", "f3", "f4", "f5", "f6", "f7", "role", "path"]

    data = defaultdict(dict)

    with open_file_safely(input_file, mode="r") as rfile:
        for line in rfile:
            if not line.strip().startswith(("#", " ")):
                key, *rest_items = line.strip().split(":")
                # use zip to iterate over several iterables in parallel to form a dictionary
                data[key] = dict(zip(key_item, rest_items))

    output_file = root / "ex23_csv2json_out.json"
    with open_file_safely(output_file, mode="w") as wfile:
        json.dump(data, wfile, sort_keys=True, separators=(",", ": "), indent=4)
