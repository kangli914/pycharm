#!/usr/bin/env python3

"""Given a list of strings, sort them according to how many vowels they contain."""

VOWEL = "aeiou"


def sort_by_vowels(word_list):

    # the variable in lambda (e.g. x) it does break a list into individual element
    # sorted(s, key=lambda x: print(f"element: {x}"))
    # element: asdefx
    # element: xrd
    # element: daraaaeeegim

    # my inital part -  not good only by specific char
    data = sorted(word_list, key=lambda x: x.lower().count("x"), reverse=True)
    print(data, end='\n\n')


    data = sorted(word_list, key=lambda word: sum(ch in VOWEL for ch in word), reverse=True)
    print(data, end='\n\n')


words = ["asdefx", "xrd", "daraaaeeegim"]
sort_by_vowels(words)
