from typing import List


class Solution:
    def check_if_number_valid(
        self, num: str, row: int, col: int, board: List[List[str]]
    ):
        # check if the nuber appears in the row
        for c in range(9):
            if board[row][c] == num:
                return False

        for r in range(9):
            if board[r][col] == num:
                return False

        # check the 3x3 grid
        row = 3 * (row // 3)
        col = 3 * (col // 3)

        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if board[r][c] == num:
                    return False

        return True

    def get_empty(self, board):
        i, j = -1, -1

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    i, j = r, c
                    break

            if i != -1:
                break

        return i, j

    def solveSudoku(self, board: List[List[int]]):
        l = [str(i) for i in range(1, 10)]

        def recurse():
            row, col = self.get_empty(board)

            if row == -1:
                return True

            for i in l:
                if self.check_if_number_valid(i, row, col, board):
                    board[row][col] = i

                    if recurse():
                        return True

                    board[row][col] = "."

            return False

        return recurse()


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


print(Solution().solveSudoku(board))

for b in board:
    print(b)
