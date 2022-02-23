#!/usr/bin/env python3

import sys

def strokes(tokens):
    return sum([int(t) for t in tokens])


def sorter(t):
    return t[-1]


def main():
    d = {}
    disq = []
    for line in sys.stdin:
        tokens = line.strip().split()
        name = ' '.join(tokens[:-3])
        try:
            d[name] = strokes(tokens[-3:])
        except ValueError:
            disq.append(name)
    for k, v in sorted(d.items(), key=sorter):
        print(f'{k:s}: {v:d}')
    if disq:
        print(f'Disqualified: {", ".join(disq):s}')


if __name__ == '__main__':
    main()
