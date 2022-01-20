#!/usr/bin/env python3

import sys

def palindrome(s):
    i = 0
    while i < len(s) and s[i] == s[len(s) - 1 - i]:
        i = i + 1
    if i == len(s):
        return True
    else:
        return False


for s in sys.stdin:
    s = s.lower()
    s = s.rstrip()
    s = s.replace(".", "")
    s = s.replace(",", "")
    s = s.replace(":", "")
    s = s.replace(" ", "")
    s = s.replace("!", "")
    s = s.replace("?", "")
    print(palindrome(s))
