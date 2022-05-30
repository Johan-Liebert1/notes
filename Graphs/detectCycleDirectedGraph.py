from collections import defaultdict

from graphql import visit


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.visited = False
        self.visiting = False


"""  
FIXME We can use graph coloring to detect odd length vs even length cycle by only taking 2 colors
"""


def detect_cycle_undirected_graph(adj: list[list[int]]):
    """
    adjacency list contains { 1: [2] } and also { 2: [1] }
    also works for directed graphs
    """

    graph = defaultdict(list)

    for from_, to in adj:
        # simulating a real adjacency list where { 1: [0] } and { 0: [1] } both exist
        graph[from_].append(to)
        graph[to].append(from_)

    print(graph)

    visited_dict = {node: 0 for node in graph}

    def detect_cycle(current, visited):
        print(f"{current = }, {visited = }")

        if visited[current] == 2:
            """
            node value is set to 1 when we start processing it, then if we come back to it from it's own adjacent node
            (which is not a cycle due to the adjacency list structure) then we will increment it to 2. If we ever come
            back to the node again, then there's  a cycle
            """
            return True

        visited[current] = 1

        print(f"{visited = }")

        for neighbor in graph[current]:
            if visited[neighbor] == 1:
                # this is the case of revisiting the node from it's neighbor, ie 1 - 2, going from 1 to 2 then from
                # 2 to 1. It's not a cycle just a byproduct of the adjacency list structure
                visited[neighbor] = 2

            else:
                # send in a copy of visited
                if detect_cycle(neighbor, visited):
                    return True

        return False

    for node in graph:
        visited_dict[node] = 1

        for neighbor in graph[node]:
            if detect_cycle(neighbor, visited_dict):
                return True

        visited_dict[node] = 0

    return False


def detect_cycle_directed_graph(adj: list[list[int]]):
    """
    adjacency list contains { 1: [2] } but { 2: [1] } only if there's a path from 2 to 1
    doesn't work for undirected graphs
    """

    graph = defaultdict(list)

    for from_, to in adj:
        # simulating a real adjacency list where { 1: [0] } and { 0: [1] } both exist
        graph[from_].append(to)

        if to not in graph:
            graph[to] = []

    print(graph)

    visited_dict = {node: False for node in graph}

    def detect_cycle(current, visited):
        print(f"{current = }, {visited = }")

        if visited[current]:
            # visited this node but we came back to it so there's a cycle
            return True

        # set the node to visited
        visited[current] = True

        print(f"{visited = }")

        for neighbor in graph[current]:
            if detect_cycle(neighbor, visited):
                return True

        # reset the node to not visited for processing of other nodes
        visited[current] = False

        return False

    for node in graph:
        visited_dict[node] = True

        for neighbor in graph[node]:
            if detect_cycle(neighbor, visited_dict):
                return True

        visited_dict[node] = False

    return False


l = [[1, 2], [2, 3], [3, 4], [1, 4]]

print(detect_cycle_directed_graph(l))
