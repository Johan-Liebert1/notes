"""  
Finds shortest path between all pairs for vertices using dynamic programing 
We keep creating adjacancy matrix[i] on the i_th iteration using the matrix created on the (i - 1)th iteration

Steps

1. Create adjacancy matrix of size V x V (V = number of vertices)
2. matrix[i][j] = weight of edge from vertex i to vertex j. Infinity if no direct edge in the beginning
3. At each step i, create a new matrix using the old matrix at step (i - 1), considering an edge going from 
vertex a -> vertex i -> vertex b. Loop number of vertices times.
"""

from typing import List


def get_adjacency_matrix(n: int, graph: List[List[int]]) -> List[List[int | float]]:
    # fmt:off
    matrix = [
        [
            float('inf') 
            if row != col else 0 # no self loops
            for col in range(n + 1)
        ] 
        for row in range(n + 1)
    ]
    # fmt:on

    for (node, neighbor, weight) in graph:
        matrix[node][neighbor] = weight

    return matrix


def floyd_warshall(n: int, graph: List[List[int]]):
    matrix = get_adjacency_matrix(n, graph)

    for iteration in range(1, n + 1):
        new_matrix = [[r for r in row] for row in matrix]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                new_matrix[i][j] = min(
                    new_matrix[i][j], matrix[i][iteration] + matrix[iteration][j]
                )

        matrix = new_matrix

    for r in new_matrix[1:]:
        print(r[1:])

    return new_matrix


from tests import test_case_3

floyd_warshall(4, test_case_3)
