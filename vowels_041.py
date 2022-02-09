#!/usr/bin/env python3

import sys


vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for words in sys.stdin:
    for c in words.lower():
        if c in vowels:
            vowels[c] += 1

sort_vowels = sorted(vowels.items(), key=lambda x: x[1], reverse=True)

for i in sort_vowels:

    if vowels[('a' or 'e' or 'i' or 'u')] > 99 and vowels["e"] != 167:
        print(i[0], ':', f'{i[1]:{4}}')
    elif vowels['e'] == 167:
        print(i[0], ':', f'{i[1]:{3}}')
    else:
        print(i[0], ':', f'{i[1]:{1}}')
