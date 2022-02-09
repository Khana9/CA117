#!/usr/bin/env python3

import sys

args = sys.argv[1]
english_numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}
english_other = {
}

with open(args) as f:
    for lines in f:
        lines = lines.rstrip().split()
        english_other[lines[0]] = lines[1]
for num in sys.stdin.readlines():
    numbers_list = []
    num = num.strip().split(" ")
    for nums in num:
        if nums != "" and nums in english_numbers:
            numbers_list.append(english_other[english_numbers[nums]])
    numbers_list = ' '.join(numbers_list)
    print(numbers_list)
