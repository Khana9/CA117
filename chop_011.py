#!/usr/bin/env python3

import sys

s = sys.stdin.readlines

def chop(s):
    return s[1:len(s) - 2]


for s in sys.stdin:
    if len(chop(s)) > 0:
        print(chop(s).strip())
