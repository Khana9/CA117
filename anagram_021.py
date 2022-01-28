#!/usr/bin/env python3

import sys

def anagram(s):
    s = s.split()
    total = 0
    for lines in s:
        lines = lines.strip()
    if len(s[1]) != len(s[0]):
        return False
    t = sorted(s[0])
    s[0] = "".join(t)
    t = sorted(s[1])
    s[1] = "".join(t)
    s[1] = "".join(t)
    if s[0] == s[1]:
        return True
    else:
        return False


for line in sys.stdin:
    print(anagram(line))
