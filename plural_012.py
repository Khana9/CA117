#!/usr/bin/env python3

import sys

a = "aeiou"

def plurals(word):
    if word[-1] == "y" and (word[-2] not in a):
        word = word.replace(word[-1:], "ies", 1)
    elif (word[-1] == "s" or word[-1] == "z" or word[-1] == "x"):
        word = word + "es"
    elif word[-2:] == "fe":
        word = word.replace(word[-2:], "ves", 1)
    elif (word[-2:] == "ch" or word[-2:] == "sh"):
        word = word + "es"
    elif word[-1] == "o":
        word = word + "es"
    elif word[-1] == "f":
        word = word.replace(word[-1:], "ves", 1)
    else:
        word = word + "s"
    return word


for word in sys.stdin:
    word = plurals(word.strip())
    print(word)
