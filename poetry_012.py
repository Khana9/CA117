#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
length = 0
for line in lines:
    if len(line) > length:
        length = len(line.strip())

for line in lines:
    line = line.strip()
    print(f'{line:^{length}}')
