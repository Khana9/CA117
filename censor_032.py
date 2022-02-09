#!/usr/bin/env python3

import sys
text = sys.argv[1]

with open(text) as f:
    list = []
    for w in f:
        list.append(w.strip())
for words in sys.stdin:
    words = words.strip()
    for letters in list:
        words = words.replace(letters, "@" * len(letters))
    print(words)
