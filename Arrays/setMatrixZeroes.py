from typing import List, Set


class Solution:
    def set_row_col_zeroes(
        self,
        row: int,
        col: int,
        matrix: List[List[int]],
        rows_set: Set[int],
        cols_set: Set[int],
    ):
        print(f"{row = }, {col = }")

        if col not in cols_set:
            cols_set.add(col)
            # set col to zeroes
            for r in range(len(matrix)):
                if r != row and r not in rows_set and matrix[r][col] == 0:
                    self.set_row_col_zeroes(r, col, matrix, rows_set, cols_set)

                matrix[r][col] = 0

        if row not in rows_set:
            rows_set.add(row)

            # set row to zeroes
            for c in range(len(matrix[0])):
                if c != col and c not in cols_set and matrix[row][c] == 0:
                    self.set_row_col_zeroes(row, c, matrix, rows_set, cols_set)

                matrix[row][c] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_set = set()
        cols_set = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (
                    matrix[row][col] == 0
                    and row not in rows_set
                    and col not in cols_set
                ):
                    self.set_row_col_zeroes(row, col, matrix, rows_set, cols_set)


sol = Solution()

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

sol.setZeroes(matrix)

for row in matrix:
    print(row)
