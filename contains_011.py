#!/usr/bin/env python3

import sys

def contains(chars, s):
    for c in chars:
        if c not in s:
            return False
        s = s.replace(c, "", 1)
    return True


lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    lines[i] = lines[i].lower().strip("\n")
    i = i + 1

for line in lines:
    [chars, s] = line.strip().split()
    print(contains(chars, s))
