"""
You're a traveller on a 2D grid. Begin in the top-left corner, have to
reach the bottom-right corner and can only move right and down.

Ways to travel if grid is m*n
"""
import sys


def grid_traveller_dp(m, n):
    table = [[1 if col == 0 or row == 0 else 0 for col in range(n)] for row in range(m)]

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[-1][-1]


def grid_traveller_recursive(rows, cols, memo={}):
    if rows == 0 or cols == 0:
        return 0

    if rows == 1 or cols == 1:
        return 1

    if (rows, cols) in memo:
        return memo[(rows, cols)]

    memo[(rows, cols)] = grid_traveller_recursive(
        rows - 1, cols, memo
    ) + grid_traveller_recursive(rows, cols - 1, memo)

    return memo[(rows, cols)]


def grid_traveller_permutation(m, n):
    import math

    facts = {}

    def f(n):
        if n in facts:
            return facts[n]

        f1 = math.factorial(n)

        facts[n] = f1

        return f1

    return int(f(m - 1 + n - 1) / (f(m - 1) * f(n - 1)))


print(grid_traveller_recursive(*[int(i) for i in sys.argv[1].split(",")]))
