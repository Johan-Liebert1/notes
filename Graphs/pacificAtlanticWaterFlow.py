"""  
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""
from typing import List, Set, Tuple


# batter approach. Start at the pacific and Atlantic ocean borders and from there reverse check which nodes can
# reach


class SolutionBetter:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        if not heights:
            return []

        reach_pacific, reach_atlantic = set(), set()

        def traverse(i: int, j: int, visited: Set[Tuple[int, int]]):
            if (i, j) in visited:
                return

            visited.add((i, j))

            for new_i, new_j in ((-1 + i, j), (1 + i, j), (i, j - 1), (i, 1 + j)):
                if (
                    0 <= new_i < rows
                    and 0 <= new_j < cols
                    and (new_i, new_j) not in visited
                ):
                    if heights[i][j] <= heights[new_i][new_j]:
                        traverse(new_i, new_j, visited)

        for i in range(rows):
            # first column, nodes that can reach this col can reach pacific ocean
            traverse(i, 0, reach_pacific)

            # last column, nodes that can reach this col can reach Atlantic ocean
            traverse(i, cols - 1, reach_atlantic)

        for j in range(cols):
            traverse(0, j, reach_pacific)
            traverse(rows - 1, j, reach_atlantic)

        return reach_pacific & reach_atlantic


# my approach slow af
# Space O(n * m) | Time O(n * m)
class Node:
    def __init__(
        self, row: int, col: int, height: int, max_rows: int, max_cols: int
    ) -> None:
        self.row = row
        self.col = col
        self.height = height
        self.can_reach_pacific = row == 0 or col == 0
        self.can_reach_atlantic = row == max_rows - 1 or col == max_cols - 1
        self.visited = False
        self.visiting = False

    def get_neighbors(self, matrix):
        n = []

        if self.row - 1 >= 0:
            n.append(matrix[self.row - 1][self.col])

        if self.col - 1 >= 0:
            n.append(matrix[self.row][self.col - 1])

        if self.row + 1 <= len(matrix) - 1:
            n.append(
                matrix[self.row + 1][self.col],
            )

        if self.col + 1 <= len(matrix[0]) - 1:
            n.append(
                matrix[self.row][self.col + 1],
            )

        return n


class Solution:
    def can_reach_pacific(self, matrix, row, col):
        if row == 0 or col == 0:
            return True

        current_node = matrix[row][col]

        for neighbor in current_node.get_neighbors(matrix):
            if neighbor.height <= current_node.height:
                if neighbor.can_reach_pacific:
                    return True

                if neighbor.visiting:
                    continue

                neighbor.visiting = True

                neighbor.can_reach_pacific = self.can_reach_pacific(
                    matrix, neighbor.row, neighbor.col
                )

                neighbor.visiting = False

                if neighbor.can_reach_pacific:
                    return True

        return False

    def can_reach_atlantic(self, matrix, row, col):
        if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
            return True

        current_node = matrix[row][col]

        for neighbor in current_node.get_neighbors(matrix):
            if neighbor.height <= current_node.height:
                if neighbor.can_reach_atlantic:
                    return True

                if neighbor.visiting:
                    continue

                neighbor.visiting = True

                neighbor.can_reach_atlantic = self.can_reach_atlantic(
                    matrix, neighbor.row, neighbor.col
                )

                neighbor.visiting = False

                if neighbor.can_reach_atlantic:
                    return True

        return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_rows = len(heights)
        max_cols = len(heights[0])

        matrix = [
            [Node(r, c, heights[r][c], max_rows, max_cols) for c in range(max_cols)]
            for r in range(max_rows)
        ]

        returning_array = []

        for r in matrix:
            for node in r:
                node.visiting = True

                node.can_reach_atlantic = self.can_reach_atlantic(
                    matrix, node.row, node.col
                )

                node.can_reach_pacific = self.can_reach_pacific(
                    matrix, node.row, node.col
                )

                node.visiting = False
                node.visited = True

                if node.can_reach_pacific and node.can_reach_atlantic:
                    returning_array.append([node.row, node.col])

        return returning_array


ans = Solution().pacificAtlantic(
    [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
)

# fmt:off
sol = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# fmt:on

print(ans == sol)
