#!/usr/bin/env python3

import sys
import string
counter = {}
banned = ["!", "?", "!", ",", "."]
for words in sys.stdin:
    for values in banned:
        words = words.replace(values, "")
    words = words.lower().strip().split(" ")
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

dict_sorted = dict(sorted(counter.items(), key=lambda x: x))

for key in dict_sorted:
    print(key, ":", dict_sorted[key])
