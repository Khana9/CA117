#!/usr/bin/env python3

import sys

def contains(first, last):
    for c in last:
        if c.isdigit():
            last = last.replace(c, "", 1)
        first = first[0].upper() + first[1:-1] + first[-1]
        last = last[0].upper() + last[1:-1] + last[-1]

    return [first, last]


emails = sys.stdin.readlines()
for email in emails:
    email = email.strip("\n")
    [first, last] = email.split("@")
    [first, last] = first.split(".")
    name = contains(first, last)
    firstname = name[0]
    lastname = name[1]
    print(firstname, lastname)
