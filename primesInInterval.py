def isPrime(n):
    if n == 1 or n == 2: return False

    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primesInInterval(a, b):
    primes = []

    new_a = (a + 1) if a % 2 == 0 else a

    for i in range(new_a, b + 1, 2):
        if isPrime(i):
            primes.append(i)

    return primes

import time

start = time.time()
print(primesInInterval(1, 1000000))
print(f"FINISHED IN {time.time() - start} seconds")