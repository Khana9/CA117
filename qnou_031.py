#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

List = []
for word in words:
    low = word.rstrip().lower()
    if low[-1] == "q":
        List.append(word.rstrip())
    else:
        i = 0
        while i < (len(low) - 1):
            if low[i] == "q" and low[i + 1] != "u":
                List.append(word.rstrip())
            i += 1

print("Words with q but no u: " + str(List))
