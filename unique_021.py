#!/usr/bin/env python3

import sys
import string

def words(s):
    dupe = []
    for c in s:
        done = c.split()
        for word in done:
            word = word.lower()
            for letter in word:
                if letter in string.punctuation:
                    word = word.replace(letter, "")
            if word not in dupe:
                dupe.append(word)
    return len(dupe) - 1


input = sys.stdin.readlines()
print(words(input))
