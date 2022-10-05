#!/usr/bin/env python3

"""Find the highest, lowest, and average test scores for each subject in each class from files."""

import json
import pathlib
import sys
from collections import defaultdict


def open_file_safely(file):
    """Open the file safely.

    Accept a filename as an argument, and exit if having the error.
    """
    try:
        return open(file)
    except OSError:
        sys.exit(f"error encounter in opening the file {file}")


def open_directory_files(dir):
    """Open the json files in the given directory.

    Using pathlib.path see more in ex17_manyway_openfile file.
    """
    path = pathlib.Path()
    return [open_file_safely(file) for file in path.glob("*/9*.json")]


def find_class_score(class_data, class_tag=""):
    """Find the score of a class given a class object

    class_data is a list of dictonary in python object for that class.
    """

    # First, add the scores based on the keys like "math", "literature" and "science"

    # option 1) try and except KeyError and class_stats_1 is a dictioanry list
    class_stats_1 = dict()
    for students_score in class_data:
        for k, v in students_score.items():
            try:
                class_stats_1[k].append(v)
            except KeyError:
                class_stats_1[k] = [v]
    # print(class_stats_1)
    # {'math': [95, 80, 68, 100, 85], 'literature': [92, 85, 90, 78, 75], 'science': [93, 79, 90, 100, 90]}

    # option 2) use default dictioanry list without worrying about key error
    class_stats_2 = defaultdict(list)
    for students_scores in class_data:
        for k, v in students_scores.items():
            class_stats_2[k].append(v)

    # Second, find the class stats like min, max and average
    print(f"class {class_tag}:")
    for k, v in class_stats_2.items():
        print(f"\tsubject {k}: min {min(v)}, max {max(v)}, average {round(sum(v)/len(v))}")


if __name__ == "__main__":

    for one_file in open_directory_files("files"):
        # de-serialize/decode: reads a JSON-encoded string from a file (e.g. json.load())
        # and returns a combination of Python objects (e.g. a list of dictionary per class/file)
        one_class = json.load(one_file)
        # serialize/encode: from Python object to a JSON string
        # print(json.dumps(one_class, indent=2))

        find_class_score(one_class, class_tag=one_file.name)
