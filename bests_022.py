#!/usr/bin/env python

import sys

file = sys.argv[1]

with open(file, "r") as f:
    f = f.readlines()


top_mark = 0
top_name = []
for line in f:
    name = 0
    mark = 0
    i = 0
    while i < len(line) and line[i] != " ":
        i = i + 1
    mark = line[0:i]
    name = line[i:-1]
    if int(mark) > int(top_mark):
        top_mark = int(mark)
        top_name = []
        top_name.append(name)
    elif int(mark) == int(top_mark):
        top_name.append(name)

for names in top_name:
    name = ','.join(top_name)
print('Best student(s):' + name)
print('Best mark:', top_mark)
