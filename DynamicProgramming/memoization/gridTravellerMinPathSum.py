"""  
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


from typing import List


class Solution:
    def paths(self, grid, row, col, cache):
        rows = len(grid)
        cols = len(grid[0])

        if row == 0 or col == 0:
            # can never reach the target if we're out of bounds
            return float("inf")

        if row == 1 and col == 1:
            return grid[-1][-1]

        if (row, col) in cache:
            return cache[(row, col)]

        cache[(row, col)] = grid[rows - row][cols - col] + min(
            self.paths(grid, row - 1, col, cache), self.paths(grid, row, col - 1, cache)
        )

        return cache[(row, col)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.paths(grid, len(grid), len(grid[0]), {})
