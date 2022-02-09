#!/usr/bin/env python3

import sys
contacts = sys.argv[1]

with open(contacts) as f:
    dict = {}
    for info in f:
        info = info.split()
        dict[info[0]] = info[1]
for names in sys.stdin:
    if names.strip() not in dict:
        print('Name: ' + names.strip())
        print('No such contact')
    else:
        print('Name: ' + names.strip())
        print('Phone: ' + dict[names.strip()])
