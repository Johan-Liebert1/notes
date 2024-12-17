"""  
Single source shortest path algo

NOTE Djikstra algo might or might not work for negative weight edges. Consider Bellman Ford algo in that case

1. Mark all vertices as unvisited initially
2. Mark all nodes with 'infinity' distance intially except the source nodes
3. Loop the following
    a. Pick the min value node which is unprocessed (minimum weight)
    b. Mark this nodes as processed ( U -> V )
    c. Update all adjacent vertices as 
        if cost[v] + weight(uv) < cost[v]: Update
        else: skip
"""

from collections import defaultdict
from typing import Dict, List, Tuple


def create_graph(input_: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
    """input_[i] = [vertex1, vertex2, weight]"""

    graph = defaultdict(list)

    for v1, v2, w in input_:
        graph[v1].append((v2, w))

        if v2 not in graph:
            graph[v2] = []

    return graph


def get_min(array: List[float], visited: List[bool]) -> Tuple[int, int | float]:
    m = float("inf")
    idx = -1

    for i, e in enumerate(array):
        if i != 0 and e < m and not visited[i]:
            m = e
            idx = i

    return (idx, m)


def djikstra(input_: List[List[int]]):
    graph = create_graph(input_)

    count = len(graph.keys()) + 1

    # use a set if graph nodes are not integers
    visited = [False] * count

    # came_from[i] -> which node did we have to go through to reach i
    came_from = [-1] * count

    distance = [float("inf")] * count
    distance[1] = 0  # node 1 is the source

    nodes_visited = 0

    while 1:
        if nodes_visited == len(visited):
            break

        # can be optimized with a heap
        index, _ = get_min(distance, visited)

        visited[index] = True
        nodes_visited += 1

        for (neighbor, weight) in graph[index]:
            if distance[neighbor] > distance[index] + weight:
                distance[neighbor] = distance[index] + weight
                came_from[neighbor] = index

    return distance, came_from


from tests import test_case_1, test_case_2

print(djikstra(test_case_1))
print(djikstra(test_case_2))
