#!/usr/bin/env python3

from sys import stdin

malachy_byrne_CASE_3_Donegal = {}  # Stored names and values in a dictionary called malachy_byrne_CASE_3_Donegal
lines = [line.strip() for line in stdin]  # Takes in line from stdin, and strips it equaled to lines

def calc(words):  # This function does the calculation and ouputs the answer
    number = 0  # This is the answer
    i = 0
    flag = 0  # This is 0 until the first calculation has been done, the next calcs only needs to be added or subtracted
    while i < len(words):  # i searches through every "word" in the list until it finds a "+" or "-" then calculates the words before and after i
        if words[i] == "+":
            if words[i - 1] in malachy_byrne_CASE_3_Donegal and words[i + 1] in malachy_byrne_CASE_3_Donegal and flag != 1:
                number = number + malachy_byrne_CASE_3_Donegal[words[i - 1]] + malachy_byrne_CASE_3_Donegal[words[i + 1]]
                flag = 1
            elif words[i - 1] in malachy_byrne_CASE_3_Donegal and words[i + 1] in malachy_byrne_CASE_3_Donegal and flag == 1:
                number = number + malachy_byrne_CASE_3_Donegal[words[i + 1]]
        if words[i] == "-":
            if words[i - 1] in malachy_byrne_CASE_3_Donegal and words[i + 1] in malachy_byrne_CASE_3_Donegal and flag != 1:
                number = malachy_byrne_CASE_3_Donegal[words[i - 1]] - malachy_byrne_CASE_3_Donegal[words[i + 1]]
                flag = 1
            elif words[i - 1] in malachy_byrne_CASE_3_Donegal and words[i + 1] in malachy_byrne_CASE_3_Donegal and flag == 1:
                number = number - malachy_byrne_CASE_3_Donegal[words[i + 1]]
        i = i + 1
    for name, number_in_dict in malachy_byrne_CASE_3_Donegal.items():  # Searches malachy_byrne_CASE_3_Donegal for the key assigned to the value.
        if int(number) == int(number_in_dict):  # If the calculated number matches a key in malachy_byrne_CASE_3_Donegal, the key is returned
            return name
    return "unknown"  # If a key is not returned, "unknown" is returned


for line in lines:
    line = line.split()  # Splits the line by space
    saved_line = " ".join(line[1:])  # Saves the line excluding the first word(for printing)
    if line[0] == "def":
        malachy_byrne_CASE_3_Donegal[line[1]] = int(line[2])  # Adds to the dictionary for def
    elif line[0] == "clear":  # Clears the dictionary
        malachy_byrne_CASE_3_Donegal = {}
    elif line[0] == "calc":  # Throws the calculation at the function expecting an output, which is printed with saved_line
        print(saved_line, calc(line))
