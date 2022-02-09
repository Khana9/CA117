#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()
def set(num):
    nums = range(1, num + 1)
    a = ['X' if int(numbers) % 3 == 0 else numbers for numbers in nums]
    print("Multiples of 3 replaced: " + str(a))


for s in nums:
    s = s.rstrip()
    set(int(s))
