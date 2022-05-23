def is_prime(n: int, primes: "dict[int, bool]") -> bool:
    if n in primes:
        return primes[n]

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        primes[n] = False
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            primes[n] = False
            return False

    primes[n] = True

    return True


def helper(
    input_str: str, start: int, cache: "dict[int, bool]", primes: "dict[int, bool]"
):
    if start > len(input_str) - 1:
        return 0

    number = input_str[start:]

    if number in cache:
        return cache[number]

    if start == len(input_str) - 1 and is_prime(int(input_str[-1]), primes):
        return 1

    ways_to_split = 0

    for i in range(start, len(input_str)):
        prefix = input_str[start:i]

        print(f"{prefix = }")

        if len(prefix) > 0 and is_prime(int(prefix), primes):
            ways_to_split_for_suffix = helper(input_str, i, cache, primes)

            print(f"suffix = {input_str[i:]}, {ways_to_split_for_suffix = }")

            ways_to_split += ways_to_split_for_suffix

            # ways_to_split = max(ways_to_split, ways_to_split_for_suffix + 1)

    cache[number] = ways_to_split

    return ways_to_split


def split_primes(input_str: str) -> int:
    cache = {}
    primes = {1: False}

    r = helper(input_str, 0, cache, primes)

    print(cache)

    return r


# print(split_primes("31173"))

print([i for i in range(1, 400) if is_prime(i, {1: False})])
