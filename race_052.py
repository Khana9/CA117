#!/usr/bin/env python3

import sys
d = {}

for lines in sys.stdin:
    [name, times] = lines.strip().split(' ', 1)
    times = times.replace(':', '').split()
    int_times = []
    for time in times:
        try:
            int_times.append(int(time))
        except ValueError:
            int_times = []
            break
    if len(int_times) > 0:
        min_time = min(int_times, key=int)
        d[min_time] = name

lowest_time = min(d.keys(), key=int)
tmp = ''
for c in str(lowest_time):
    if len(tmp) != 1:
        tmp = tmp + c
    else:
        tmp = tmp + ':' + c
print(f'{d[lowest_time]} : {tmp}')
