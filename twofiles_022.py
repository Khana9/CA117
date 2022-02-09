#!/usr/bin/env python3

import sys
a = []

with open(sys.argv[1], "r") as f:
   for o in f:
      s = o.strip()
      a.append(int(s))
with open(sys.argv[2], "r") as w:
   for o in w:
      s = o.strip()
      a.append(int(s))
i = 0
while i < len(a) // 2:
   print(a[i])
   print(a[i + len(a) // 2])
   i = i + 1
