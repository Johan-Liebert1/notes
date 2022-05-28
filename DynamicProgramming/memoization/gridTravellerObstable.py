"""  
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""


class Solution:
    def paths(self, grid, row, col, cache):
        rows, cols = len(grid), len(grid[0])

        if row == 0 or col == 0:
            return 0

        if row == 1:
            # at the final row. Check whether there's any obstable between the current column and the final column
            i = cols - col

            while i < cols:
                if grid[-1][i] == 1:
                    return 0

                i += 1

            return 1

        if col == 1:
            i = rows - row

            while i < rows:
                if grid[i][-1] == 1:
                    return 0

                i += 1

            return 1

        if (row, col) in cache:
            return cache[(row, col)]

        right, down = 0, 0

        if grid[rows - row][cols - col + 1] != 1:
            # can go right
            right = self.paths(grid, row, col - 1, cache)

        if grid[rows - row + 1][cols - col] != 1:
            # can go down
            down = self.paths(grid, row - 1, col, cache)

        cache[(row, col)] = right + down

        return right + down

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        return self.paths(obstacleGrid, len(obstacleGrid), len(obstacleGrid[0]), {})
