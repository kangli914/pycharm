#!/user/bin/env python3

"""Find the word from a list of words with the greatest number of repeated vowels"""

from collections import Counter
# https://www.youtube.com/watch?v=n_g_uZf65EQ
# collections is a module and, Counter is a class in the collections module

words = ['thiiiooouuus', 'iss', 'an', 'elementary', 'test', 'example', 'nrdstp']
VOWEL = "aeiou"


def most_repeating_letters_in_word(word):
    """Return the sum of occurence of vowel in a word."""

    sum = 0
    for item in Counter(word).most_common():
        if item[0] in VOWEL:
            sum += item[1]
    return sum


# print(most_repeating_letters_in_word("worddadeusss"))
print(sorted(words, key=most_repeating_letters_in_word, reverse=True))
