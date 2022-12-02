#!/usr/bin/env python3

"""Output vowels and consonants into different files given a input file."""

import os
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely and return the file wrapper when no error."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error(f"having issue opening the file {file}!")


if __name__ == "__main__":
    path = Path("files")
    rfile = path / "ex18_vowel.txt"
    vowels_file = path / "ex24_vowels.txt"
    consonants_file = path / "ex24_consonants.txt"

    with open_file_safely(rfile) as rfile, open_file_safely(vowels_file, mode="w") as vovels, open_file_safely(consonants_file, mode="w") as consonants:

        # for line in rfile:
        #     for words in line.strip().split():
        #         for char in words:
        #             print(char)

        # List Comprehension
        vovels.writelines([char for line in rfile
                    for word in line.strip().split()
                    for char in word.strip() if char in ("a", "e", "i", "o", "u")])
