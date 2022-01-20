#/usr/bin/env python3

import sys

file = sys.argv[1]
err = 0

with open(file, "r") as f:
    f = f.readlines()

    top_mark = 0
    top_name = 0
    for line in f:
        name = 0
        mark = 0
        try:
            i = 0
            while i < len(line) and line[i] != " ":
                i = i + 1
            mark = line[0:i]
            name = line[i:-1]
            if int(mark) > int(top_mark):
                top_mark = int(mark)
                top_name = name
        except ValueError:
            err = 1
            print('Invalid mark', mark, 'encountered. Exiting.')
if err == 0:
    print('Best student:', top_name.strip())
    print('Best mark:', top_mark)
