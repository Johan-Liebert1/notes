"""  
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
"""


from typing import List


class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:

        for idx in range(len(nums) - 2, -1, -1):

            row = nums[idx]

            for pos, _ in enumerate(row):

                next_row = nums[idx + 1]

                adjacent = self.get_adjacent(next_row, pos)

                row[pos] += min(adjacent)

        return nums[0][0]

    def get_adjacent(next_row, pos):
        return [next_row[pos], next_row[pos + 1]]

    # my sol (kinda slow)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle) - 1

        if len(triangle) == 1:
            return triangle[0][0]

        # (row, col) -> minimum sum from that row col to the end
        cache = {}

        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            if row == height - 1:
                cache[(row, col)] = triangle[row][col] + min(
                    triangle[row + 1][min(col + 1, len(triangle[row]))],
                    triangle[row + 1][col],
                )

                return cache[(row, col)]

            first = triangle[row][col] + dfs(row + 1, col)
            second = triangle[row][col] + dfs(row + 1, col + 1)

            cache[(row, col)] = min(first, second)

            return min(first, second)

        dfs(0, 0)

        return cache[(0, 0)]
