def recurFib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = recurFib(n - 1, memo) + recurFib(n - 2, memo)

    return memo[n]


print(recurFib(50))
