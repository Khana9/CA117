#!usr/bin/env python3

import sys
def classes(paswords):
    digit = 0
    upper = 0
    lower = 0
    other = 0
    for c in paswords:
        if c.islower():
            upper = 1
        elif c.isupper():
            lower = 1
        elif c.isdigit():
            digit = 1
        else:
            other = 1
    total = digit + upper + lower + other
    return total


for password in sys.stdin.readlines():
    print(classes(password.rstrip("\n")))
