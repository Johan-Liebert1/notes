from typing import List, Tuple

# solve it using graph coloring approach
# if we ever find a '1' we'll visit all the connected '1's in one go and count that as a single huge island
# that way we'll never visit those islands again as we'll set the visited dots to '2'
def numIslands(grid: List[List[str]]) -> int:
    total = 0

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] != "1":
            return

        if grid[row][col] == "1":
            grid[row][col] = "2"

        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                total += 1

    return total


# slow af
class Solution:
    def get_neighbors(self, pos: Tuple[int], rows: int, cols: int) -> Tuple[int]:
        n = []

        cr, cc = pos
        row_adders = [-1, 0, 1]
        col_adders = [[0], [-1, 1], [0]]

        for (ri, ra) in enumerate(row_adders):
            if 0 <= cr + ra < rows:
                col_add = col_adders[ri]

                for ca in col_add:
                    if 0 <= cc + ca < cols:
                        n.append((cr + ra, cc + ca))

        return n

    def numIslands(self, grid: List[List[str]]) -> int:
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        visited = set()
        queue = []
        index_into_queue = 0
        num_islands = 0

        for row in range(grid_rows):
            for col in range(grid_cols):
                if (row, col) in visited or grid[row][col] == "0":
                    continue

                queue.append((row, col))
                visited.add((row, col))

                while index_into_queue < len(queue):
                    pos = queue[index_into_queue]
                    index_into_queue += 1

                    for n in self.get_neighbors(pos, grid_rows, grid_cols):
                        if n not in visited and grid[n[0]][n[1]] != "0":
                            visited.add(n)
                            queue.append(n)

                num_islands += 1

        return num_islands
