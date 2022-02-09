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
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fiftheen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'one hundred'
}


for num in sys.stdin.readlines():
    numbers_list = []
    num = num.strip().split(" ")
    for nums in num:
        if nums != "" and nums in numbers:
            numbers_list.append(numbers[nums])
        elif len(nums) == 2:
            first_num = nums[0]
            first_num = nums[0] + "0"
            second_num = nums[1]
            numbers_list.append(numbers[first_num] + "-" + numbers[second_num])
    numbers_list = ' '.join(numbers_list)
    print(numbers_list)
