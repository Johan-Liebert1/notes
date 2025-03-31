"""  
Single source shortest path algo

It's a dynamic programing appraoch wherein we check all possibilities. 

If there are E edges and V vertices, then we perform relaxation on all edges (V - 1) times

Time complexity : minimum -> O(n ^ 2)

maximum (in a complete graph) = O(n ^ 3)

NOTE
Drawback

If total weight of a cycle is negative in a graph, then Bellman Ford fails 

Bellman Ford can check for a negative weight cycle as something will change in a negative weight cycle on the Vth relaxation

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


def bellman_ford(input_: List[List[int]]):
    graph = create_graph(input_)

    count = len(graph.keys()) + 1

    distance = [float("inf")] * count
    distance[1] = 0  # node 1 is the source

    for _ in range(len(graph.keys()) - 1):
        for node in graph:
            for (neighbor, weight) in graph[node]:
                if distance[neighbor] > distance[node] + weight:
                    distance[neighbor] = distance[node] + weight

    return distance


from tests import test_case_1, test_case_2

print(bellman_ford(test_case_1))
print(bellman_ford(test_case_2))
