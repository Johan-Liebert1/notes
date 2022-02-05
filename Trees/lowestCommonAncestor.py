"""  
Given a tree where a node can have many children, and given three inputs, the root node and two more nodes, find the 
common ancestor of the two nodes

class Node:
    def __init__(self):
        self.children: list[Node] = []
"""


class TreeNode:
    pass


class Node:
    def __init__(self, lowest_common_ancestor, num_children) -> None:
        self.lowest_common_ancestor: Node = lowest_common_ancestor
        self.num_children: int = num_children


def get_common_ancestory(root, node1, node2):
    return recursive_func(root, node1, node2)


def recursive_func(root: TreeNode, node1: TreeNode, node2: TreeNode) -> Node:
    imp_children = 0

    for child in root.children:
        children_info = recursive_func(child, node1, node2)

        if children_info.num_children is not None:
            return children_info

        imp_children += children_info.num_children

    if root == node1 or root == node2:
        imp_children += 1

    lowest_common_ancestor = root if imp_children == 2 else None

    return lowest_common_ancestor
