'''
You're a traveller on a 2D grid. Begin in the top-left corner, have to
reach the bottom-right corner and can only move right and down.

Ways to travel if grid is m*n
'''
import sys


def grid_traveller(rows, cols, memo={}):
    if rows == 0 or cols == 0:
        return 0

    if rows == 1 or cols == 1:
        return 1

    if (rows, cols) in memo:
        return memo[(rows, cols)]

    memo[(rows, cols)] = grid_traveller(rows - 1, cols, memo) + grid_traveller(rows, cols - 1, memo)

    return memo[(rows, cols)]


print(grid_traveller(*[int(i) for i in sys.argv[1].split(',')]))
