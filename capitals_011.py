#!/usr/bin/env python3

import sys


def cap(s):
        return s[0].upper() + s[1:-1] + s[-1].upper()


for s in sys.stdin:
    s = s.strip()
    if len(s) > 1:
        print(cap(s))
