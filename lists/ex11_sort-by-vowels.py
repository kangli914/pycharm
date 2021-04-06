#!/usr/bin/env python3

"""Given a list of strings, sort them according to how many vowels they contain."""

VOWEL = "aeiou"


def sort_by_vowels(s):
    data = sorted(s, key=lambda x: x.lower().count(VOWEL))
    print(data)

s = ["asdefx", "xrd", "daraaaeeegim"]
sort_by_vowels(s)
