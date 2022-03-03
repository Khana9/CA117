#!/usr/bin/env python3

import sys

input = sys.stdin.readlines()

for term in input:
    term = term.strip().split()
    input2int = [int(number) for number in term]
    a, b, c = input2int

    num1 = -b + (((b ** 2) - (4 * a * c)) ** 0.5)
    num2 = -b - (((b ** 2) - (4 * a * c)) ** 0.5)
    d = 2 * a
    root1 = num1 / d
    root2 = num2 / d

    root1_test = (a * (root1) ** 2) + (b * root1) + c
    root2_test = (a * (root2) ** 2) + (b * root2) + c

    if root1_test == 0 and root2_test == 0:
        print(f"r1 = {root1}, r2 = {root2}")
    else:
        print("None")
