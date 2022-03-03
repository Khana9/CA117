#!/usr/bin/env python3

import sys

def nice(s):
    tokens = ['n', 'i', 'c', 'e']
    for t in tokens:
        if s.count(t) != 1:
            return False
    return True

def order(s):
    tokens = ['n', 'i', 'c', 'e']
    n1 = 0
    n2 = 1
    while n2 < len(tokens):
        if (s.find(tokens[n1])) > (s.find(tokens[n2])):
            return False
        n1 += 1
        n2 += 1
    return True


for line in sys.stdin:
    line = line.strip()
    if nice(line):
        if order(line):
            print(line)
