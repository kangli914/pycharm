#!/usr/bin/env python3

"""encript and decript the files using python build in functions ord()/chr()"""


import os
from pathlib import Path


def open_file_safely(file, mode="r"):
    """Open file safely and return the file wrapper when no error."""
    try:
        return open(file, mode=mode)
    except OSError:
        os.error(f"having issue openning the file {file}!")


def encrypt(rfile, wfile):
    """encrypt the text in given file."""

    if rfile.exists():
        with open_file_safely(rfile) as reader, open_file_safely(wfile, mode="w") as writer:
            for line in reader:
                for words in line.split():
                    for char in words:
                        writer.write(f"{ord(char)}")
                    writer.write(" ")
                writer.write("\n")


def decrypt(rfile):
    """decrypt the text in given file."""

    if rfile.exists():
        with open_file_safely(rfile) as reader:


    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
    return ''.join(characters)


if __name__ == "__main__":
    # root = Path.cwd()
    path = Path("files")
    rfile = path / "ex18_vowel.txt"
    wfile = path / "ex24_encript.txt"

    encrypt(rfile, wfile)
    decrypt(wfile)
