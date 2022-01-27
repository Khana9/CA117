#!/usr/bin/env python3

import sys
for lines in sys.stdin:
    num = [int(n) for n in range(2, (int(lines) + 1))]
    prime = [n for n in num if all(n % p != 0 for p in range(2, (n // 2) + 1))]
    print(f'Primes: {prime}')
