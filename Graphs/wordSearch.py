from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def out_of_bounds(row, col):
            return not (row > -1 and row < len(board) and col > -1
                        and col < len(board[0]))

        def dfs(row, col, index):
            if (row, col) in visited or out_of_bounds(
                    row, col
            ) or index >= len(word) or word[index] != board[row][col]:
                return False

            if index == len(word) - 1 and word[index] == board[row][col]:
                return True

            visited.add((row, col))

            u = dfs(row + 1, col, index + 1)
            d = dfs(row - 1, col, index + 1)
            l = dfs(row, col + 1, index + 1)
            r = dfs(row, col - 1, index + 1)

            visited.remove((row, col))

            return u or d or l or r

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False


sol = Solution()
# fmt:off
print(
    'exists = ',
    sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"],
               ["A", "D", "E", "E"]],
        word='ABCESEEEFS',
    ))
