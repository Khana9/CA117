#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
for line in s:
    line = line.rstrip()
    line = line.replace("m", "M", 1)
    print(line)
