from collections import defaultdict


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

    visited_dict = {node: False for node in graph}

    # NOTE this thing is too slow for large grpahs. For better performance keep track
    # of nodes we've visited and nodes we're visiting
    # see courseSchedule.py for that
    def detect_cycle(current, visited):
        if visited[current]:
            # visited this node but we came back to it so there's a cycle
            return True

        # set the node to visited
        visited[current] = True

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


# fmt:off
l = [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]]

print(detect_cycle_directed_graph(l))
