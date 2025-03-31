# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        stack = [node]
        nodes = {node.val: Node(node.val)}

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)

                nodes[curr.val].neighbors.append(nodes[neighbor.val])

        return nodes[node.val]

    def cloneGraphDfs(self, node: "Node") -> "Node":
        if not node:
            return node

        new_node = Node(node.val)

        visited = set()

        visited.add(node.val)

        nodes = {node.val: new_node}

        def dfs(old_node: "Node", new_node: "Node"):
            for n in old_node.neighbors:
                new_new_node = None

                if n.val in nodes:
                    new_new_node = nodes[n.val]
                else:
                    new_new_node = Node(n.val)
                    nodes[n.val] = new_new_node

                new_node.neighbors.append(new_new_node)

                if n.val not in visited and len(n.neighbors) > 0:
                    visited.add(n.val)
                    dfs(n, new_node.neighbors[-1])

        dfs(node, new_node)

        return new_node
