class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.visited = False
        self.visiting = False


def dfs_traverse(node: Node):
    """
    Traverses a node in DFS manner and returns a bool indicating whether it found a cycle or not
    """
    if node.visited:
        return False

    if node.visiting:
        # we have a cycle
        return True

    node.visiting = True

    for prereq_node in node.neighbors:
        contains_cycle = dfs_traverse(prereq_node)

        if contains_cycle:
            return True

    node.visited = True
    node.visiting = False

    return False
