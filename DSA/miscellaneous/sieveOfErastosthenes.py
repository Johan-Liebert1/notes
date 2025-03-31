# prime numbers up to n

import sys

n = 50 if len(sys.argv) < 2 else int(sys.argv[1])

primes = [True for _ in range(n + 1)]

for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
        for j in range(i*i, n + 1, i):
            primes[j] = False


print([i for i in range(n + 1) if primes[i]])
