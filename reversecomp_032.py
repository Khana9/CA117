#!/usr/bin/env python3

'''Identify words whose reverse is also in the dictionary.'''

import sys

# Binary search (adapted from CA116)
def binsearch(query, sorted_list):

    '''Return True if query in sorted_list else False'''

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1

        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False


def main():

    # Build the list of words
    liness = [line.strip() for line in sys.stdin]

    # Build the sorted list of words
    sl = sorted([w.lower() for w in liness])

    # Words whose reverse is in the list (binsearch)
    revs = [w for w in liness if len(w) >= 5 and binsearch(w[::-1].lower(), sl)]

    # Word whose reverse is in the list (brute-force search is too slow)
    # revs = [w for w in l if len(w) >= 5 and w[::-1].lower() in sl]

    print(revs)


if __name__ == "__main__":
    main()
