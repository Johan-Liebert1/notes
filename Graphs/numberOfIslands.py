"""  
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water. 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List, Tuple


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
        index_into_queue = -1
        num_islands = 0

        for row in range(grid_rows):
            for col in range(grid_cols):
                if (row, col) in visited or grid[row][col] == "0":
                    continue

                queue.append((row, col))
                visited.add((row, col))
                index_into_queue += 1

                while index_into_queue < len(queue):
                    pos = queue[index_into_queue]
                    index_into_queue += 1

                    for n in self.get_neighbors(pos, grid_rows, grid_cols):
                        if n not in visited and grid[n[0]][n[1]] != "0":
                            visited.add(n)
                            queue.append(n)

                num_islands += 1

        return num_islands


sol = Solution()

print(
    sol.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
