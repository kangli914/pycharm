#!/usr/bin/env python3

"""convert /etc/passwd from CSV to JSON file.
The JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file
"""

import json
import os
import pathlib


def open_file_safe(file, mode="r"):
    """Open file safely and return the file wrapper or the error."""

    try:
        return open(file, mode)
    except OSError:
        os.error(f"error encounterred when opening the {file}!")


if __name__ == "__main__":
    root_dir = pathlib.Path("files")
    ifile = root_dir / "ex18_faked_pd.txt"

    data = {}

    if ifile.exists():

        with open_file_safe(ifile) as f:
            for line in f:
                if not line.strip().startswith(("#", "\n")):
                    # print(line)
                    key, *rest = line.strip().split(":")
                    try:
                        data[key].append(rest)
                    except KeyError:
                        # rest here is alreay a list
                        data[key] = rest

        # print(data)

        wfile = root_dir / "ex23_csv2json_out.json"
        with open_file_safe(wfile, mode="w") as f:
            json.dump(data, f, sort_keys=True, separators=(",", ": "), indent=2)
