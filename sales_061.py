#!/usr/bin/env python3

import sys

def sale(ls):
    total = sum([int(t) for t in ls]) / len(ls)
    return total

def tagger(t):
    return(t[1])


ans = {}
for line in sys.stdin:
    toke = line.strip().split(':')
    name, sales = toke[0], toke[1].split(',')
    sales = [v.strip() for v in sales]
    total = (sale(sales))
    ans[name] = total

for k, v in sorted(ans.items(), key=tagger, reverse=1):
    print(f'{k}: {v:.2f}')
