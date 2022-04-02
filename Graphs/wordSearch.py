from typing import List


class Solution:
    def get_neighbors(self, pos: List[int], rows: int, cols: int) -> List[int]:
        n = []

        cr, cc = pos
        row_adders = [-1, 0, 1]
        col_adders = [[0], [-1, 1], [0]]

        for (ri, ra) in enumerate(row_adders):
            if 0 <= cr + ra < rows:
                col_add = col_adders[ri]

                for ca in col_add:
                    if 0 <= cc + ca < cols:
                        n.append([cr + ra, cc + ca])

        return n

    def search(self, board: List[List[str]], word: str, start: List[int]) -> bool:
        visited = set()

        num_rows, num_cols = len(board), len(board[0])

        i = 0
        stack = [start]
        aux_stack = [start]

        while len(stack) > 0:
            # print(f"\n\n{word = }, {i = }, {stack = }")
            pos = stack.pop()

            row, col = pos
            print(f"{row = }, {col = }, {board[row][col] = }")

            visited.add((row, col))

            if board[row][col] == word[i]:
                # print(f"{word[i] = }, {row = }, {col = }, {board[row][col] = }")
                i += 1

            if i == len(word):
                break

            neighbors = self.get_neighbors(pos, num_rows, num_cols)

            # print(f"{row = }, {col = }, {neighbors = }")

            for n in neighbors:
                nr, nc = n

                # print(f"{ board[nr][nc] = }, { word[i] = }")

                if (nr, nc) in visited:
                    continue

                if board[nr][nc] == word[i]:
                    stack.append(n)
                    aux_stack.append(n)

        for [row, col] in aux_stack:
            print(board[row][col], (row, col), end=" -> ")

        print("\n")

        return i == len(word)

    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starts.append([i, j])

        if len(word) == 1 and len(starts) > 0:
            return True

        for start in starts:
            if self.search(board, word, start):
                return True

        return False


sol = Solution()

# fmt:off
print('exists = ', sol.exist(
    board=[
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ],
    word='ABCESEEEFS',
))
