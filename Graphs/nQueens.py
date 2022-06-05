from typing import List

sol = []


class Solution:
    def is_cell_under_attack(self, row: int, col: int, board: List[List[str]]) -> bool:
        i = 1

        # go top left and top right to find a queen
        for r in range(row - 1, -1, -1):
            left = col - i
            right = col + i

            if left > -1 and board[r][left] == "Q":
                return True

            if right < len(board[0]) and board[r][right] == "Q":
                return True

            i += 1

        return False

    def solveNQueens(self, n: int = 4) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]

        rows_under_attack = set([0])
        cols_under_attack = set()

        def recurse(row: int) -> bool:
            if row == n:
                return True

            if row in rows_under_attack:
                return False

            all_cols_under_attack = True

            for col in range(n):
                if col in cols_under_attack:
                    continue

                if self.is_cell_under_attack(row, col, board):
                    continue

                all_cols_under_attack = False

                board[row][col] = "Q"
                cols_under_attack.add(col)
                rows_under_attack.add(row)

                if row + 1 == n:
                    break

                recurse(row + 1)

                board[row][col] = "."
                cols_under_attack.remove(col)
                rows_under_attack.remove(row)

            if row == n - 1 and not all_cols_under_attack:
                sol.append([[char for char in row] for row in board])
                board[row][col] = "."
                cols_under_attack.remove(col)
                rows_under_attack.remove(row)

            return not all_cols_under_attack

        for c in range(n):
            board[0][c] = "Q"
            cols_under_attack.add(c)

            recurse(1)

            board[0][c] = "."
            cols_under_attack.remove(c)


Solution().solveNQueens(8)

for b in sol:
    for r in b:
        print(r)

    print()
