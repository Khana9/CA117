#!/usr/bin/env python3

import sys

numbers = {
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


for num in sys.stdin.readlines():
    numbers_list = []
    num = num.strip().split(" ")
    for nums in num:
        if nums != "" and nums in numbers:
            numbers_list.append(numbers[nums])
        else:
            numbers_list.append("unknown")
    numbers_list = ' '.join(numbers_list)
    print(numbers_list)
