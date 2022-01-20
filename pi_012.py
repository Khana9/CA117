#!/usr/bin/env python3

import sys
import math

points = sys.stdin.readlines()
for point in points:
    point = point.rstrip()
    print(f'{math.pi:.{point}f}')
