#!/usr/bin/env python3

import sys

y = sys.stdin.readline()
y = y.strip().split()

i = 0
while i < len(y) - 1:
    p = i
    j = i + 1
    while j < len(y):
        if int(y[j]) < int(y[p]):
            p = j
        j = j + 1
    tmp = y[p]
    y[p] = y[i]
    y[i] = tmp
    i = i + 1

A = y[0]
B = y[1]
C = y[2]

order = sys.stdin.readline().strip()

string = ""
for i in order:
    if i == "C":
        string = string + C + " "
    if i == "B":
        string = string + B + " "
    if i == "A":
        string = string + A + " "

print(string.strip())
