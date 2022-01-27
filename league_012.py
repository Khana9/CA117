#!/usr/bin/env python3

'''Print a formatted league table.'''

import sys

h1 = 'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip().split())

    clubs = []
    for line in lines:
        clubs.append(' '.join(line[1:-8]))

    max_width = 0
    for club in clubs:
        if len(club) > max_width:
            max_width = len(club)

    print(
        f'{h1:>3s} {h2:{max_width:d}s} {h3:>2s} {h4:>3s} '
        f'{h5:>3s} {h6:>3s} {h7:>3s} {h8:>3s} {h9:>3s} {h10:>3s}')

    for line in lines:
        pos = int(line[0])
        club = ' '.join(line[1:-8])
        played = int(line[-8])
        won = int(line[-7])
        drawn = int(line[-6])
        lost = int(line[-5])
        gf = int(line[-4])
        ga = int(line[-3])
        gd = int(line[-2])
        pts = int(line[-1])
        print(
            f'{pos:3d} {club:{max_width:d}s} {played:2d} {won:3d} '
            f'{drawn:3d} {lost:3d} {gf:3d} {ga:3d} {gd:3d} {pts:3d}')


if __name__ == '__main__':
    main()
