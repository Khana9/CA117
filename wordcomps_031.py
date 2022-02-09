#!/usr/bin/env python3

'''List comprehensions based on a list of words.'''

import sys

def main():

    # Build the list of words
    liness = [line.strip() for line in sys.stdin]

    # Length 17
    words_17 = [w for w in liness if len(w) == 17]
    print(f'Words containing 17 letters: {words_17}')

    # Length 18+
    words_long = [w for w in liness if len(w) > 17]
    print(f'Words containing 18+ letters: {words_long}')

    # Four a's
    words_four_as = [w for w in liness if w.lower().count('a') == 4]
    print(f'Words with 4 a\'s: {words_four_as}')

    # 2+ q's
    words_two_qs = [w for w in liness if w.lower().count('q') >= 2]
    print(f'Words with 2+ q\'s: {words_two_qs}')

    # All words that contravene 'i before e except after c'
    words_cie = [w for w in liness if 'cie' in w.lower()]
    print(f'Words containing cie: {words_cie}')

    # All anagrams of 'angle'
    anagrams = [w for w in liness if sorted(
        w.lower()) == sorted('angle') and w.lower() != 'angle']
    print(f'Anagrams of angle: {anagrams}')


if __name__ == "__main__":
    main()
