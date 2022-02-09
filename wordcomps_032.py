#!/usr/bin/env python3

'''List comprehensions based on a list of words.'''

import sys

def allvowels(w):
    '''Return True if w contains all vowels and False otherwise.'''
    return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w

def main():

    # Build the list of words
    liness = [line.strip() for line in sys.stdin]

    # Find shortest word containing each of aeiou
    words_allvowels = [w for w in liness if allvowels(w.lower())]
    print(f'Shortest word containing all vowels: '
          f'{min(words_allvowels, key=len)}')

    # All words ending in 'iary'
    words_iary = [w for w in liness if w.lower().endswith('iary')]
    print(f'Words ending in iary: {len(words_iary)}')

    # Count ee's in every word and take the maximum
    most_ees = max([w.lower().count('e') for w in liness])

    # Extract words containing the maximum number of ee's
    words_most_ees = [w for w in liness if w.lower().count('e') == most_ees]
    print(f'Words with most e\'s: {words_most_ees}')


if __name__ == "__main__":
    main()
