#!/usr/bin/env python3

import sys

for s in sys.stdin:
    if len(s) % 2 - 1 == 0:
        print("No middle character!")
    else:
        print(s[(len(s) // 2 - 1)])
