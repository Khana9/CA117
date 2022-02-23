#!/usr/bin/env python3

import sys

def upper(s):
    letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper = [letter for letter in s if letter in letters_upper]
    a = "".join(upper)
    if 'A' in a:
        a = a.replace('A', '')
    print(a)


for lines in sys.stdin:
    upper(lines)
