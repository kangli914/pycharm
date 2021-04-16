#!/usr/bin/env python3

"""Write a function, most_repeating_word, that takes a sequence of strings as input. The
function should return the string that contains the greatest number of repeated let-
ters."""

from collections import Counter
# https://www.youtube.com/watch?v=n_g_uZf65EQ
# collections is a module and, Counter is a class in the collections module


def most_repeating_letters_in_word(word):
    """Return the count for the most occurences of the leter in given word"""

    return Counter(word).most_common(1)[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letters_in_word)
    #return sorted(words, key=most_repeating_letters_in_word)[-1]

words = ['this', 'iss', 'an', 'elementary', 'test', 'example']
# most_repeating_word(words)
# print(most_repeating_letters_in_word("aa1abc"))
print(most_repeating_word(words))