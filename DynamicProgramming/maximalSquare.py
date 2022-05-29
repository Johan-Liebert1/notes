from typing import List

"""  
exact same apporach as mine, but instead of treating this as a graph problem we're treating this
as a dp problem
"""


def maximalSquare(matrix: List[List[str]]) -> int:
    table = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

    largest = 0

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            # we can only extend diagonally downwards if the upper diagonal element is a 1
            # if it's a 0 then we can't use that in our square
            if matrix[i - 1][j - 1] == "1":
                table[i][j] = 1 + min(
                    table[i - 1][j - 1],
                    table[i - 1][j],
                    table[i][j - 1],
                )

                if table[i][j] > largest:
                    largest = table[i][j]

    return largest * largest


class Solution:
    def in_bounds(self, start, matrix):
        r, c = start
        return -1 < r < len(matrix) and -1 < c < len(matrix[0])

    def diags(self, matrix: List[List[str]], start: List[int], diag_num: int) -> int:
        r, c = start

        if not self.in_bounds([r, c], matrix):
            return diag_num - 1

        if matrix[r][c] == "0":
            return diag_num - 1

        if diag_num == 1:
            if not self.in_bounds([r + 1, c + 1], matrix):
                return diag_num

            if matrix[r + 1][c + 1] != "1":
                return diag_num

            return self.diags(matrix, [r + 1, c + 1], diag_num + 1)

        l = c - 1
        u = r - 1
        i = 1

        while i < diag_num:
            if matrix[r][l] != "1" or matrix[u][c] != "1":
                return diag_num - 1

            l -= 1
            u -= 1
            i += 1

        return self.diags(matrix, [r + 1, c + 1], diag_num + 1)

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # { (top_left_x, top_left_y) : (bottom_right_x, bottom_right_y) }
        visited = {}

        maxx = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    num_diags = self.diags(matrix, [r, c], 1)
                    visited[(r, c)] = (r + num_diags - 1, c + num_diags - 1)
                    maxx = max(maxx, num_diags)

        return maxx * maxx


print(
    Solution().maximalSquare(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "1"],
        ]
    )
)
