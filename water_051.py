#!/usr/bin/env python3

import sys

list = sys.stdin.readlines()
list[0] = list[0].strip("\n")
water = int(list[0])
buckets = 0
list = list[1].split()
for n in list:
    if int(n) <= water:
        water = water - int(n)
        buckets = buckets + 1
    else:
        break
print(buckets)
