#!/usr/bin/env python3

import sys

max_rooms = 0
for lines in sys.stdin:
    lines = lines.rstrip().split(" ")

for numbers in lines:
    if int(numbers) > max_rooms:
        max_rooms = int(numbers)
i = 0
while i < len(lines):
    lines[i] = int(lines[i])
    i = i + 1
x = range(1, max_rooms)
flag = 0
for rooms in x:
    if rooms not in lines:
        print(rooms)
        flag = 1
if flag == 0:
    print("no room")
