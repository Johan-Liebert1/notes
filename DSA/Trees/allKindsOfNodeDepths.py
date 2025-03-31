_ = """  
calculate the depth of each node in a binary tree and return the sum. Every node's depth sum 
is the sum of all it's children nodes

                             1
                           /   \
                          2     3
                         / \   / \
                        4   5 6   7
                       / \
                      8   9

depth of 4 = 2 as, depth of 8 and 9 in the binaryTree tree rooted at 4 are 1 and 1 respectively. 

depth of 2 = 6 as, depth of 4 = 1, 5 = 1, 8 = 2 and 9 = 2 relative to node 2 so depth = 2 + 2 + 1 + 1 = 6

"""

from binaryTree import Node

# O(n) time | O(n) space
def all_kinds_of_node_depths(root: Node):
    # num nodes in every sub tree
    node_counts: dict[Node, int] = {}

    add_node_counts(root, node_counts)

    node_depths: dict[Node, int] = {}

    add_node_depths(root, node_depths, node_counts)

    return node_depths(root, node_depths)


def node_depths(rootNode: Node, node_depths: dict[Node, int]):
    if rootNode is None:
        return 0

    return (
        node_depths[rootNode]
        + all_kinds_of_node_depths(rootNode.left, node_depths)
        + all_kinds_of_node_depths(rootNode.right, node_depths)
    )


def add_node_depths(
    node: Node, node_depths: dict[Node, int], node_counts: dict[Node, int]
):
    # leaf nodes have a depth of 0
    node_depths[node] = 0

    if node.left is not None:
        add_node_depths(node.left, node_depths, node_counts)
        node_depths[node] += node_depths[node.left] + node_counts[node.left]

    if node.right is not None:
        add_node_depths(node.right, node_depths, node_counts)
        node_depths[node] += node_depths[node.right] + node_counts[node.right]


def add_node_counts(node: Node, node_counts: dict[Node, int]):
    # every node has a count of at least 1
    node_counts[node] = 1

    if node.left is not None:
        add_node_counts(node.left, node_counts)
        node_counts[node] += node_counts[node.left]

    if node.right is not None:
        add_node_counts(node.right, node_counts)
        node_counts[node] += node_counts[node.right]


class TreeInfo:
    def __init__(
        self, num_nodes_in_tree: int, sum_of_depths: int, sum_of_all_depths: int
    ) -> None:
        self.num_nodes_in_tree: int = num_nodes_in_tree
        self.sum_of_depths: int = sum_of_depths
        self.sum_of_all_depths: int = sum_of_all_depths


# O(n) time | O(1) space
def all_kinds_of_node_depths_better_space(root: Node):
    return get_tree_info(root).sum_of_all_depths


def get_tree_info(tree: Node) -> TreeInfo:
    if tree is None:
        return TreeInfo(0, 0, 0)

    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)

    num_nodes_in_tree = (
        1 + left_tree_info.num_nodes_in_tree + right_tree_info.num_nodes_in_tree
    )

    sum_of_left_depths = left_tree_info.sum_of_depths + left_tree_info.num_nodes_in_tree

    sum_of_right_depths = (
        right_tree_info.sum_of_depths + right_tree_info.num_nodes_in_tree
    )

    sum_of_depths = sum_of_left_depths + sum_of_right_depths

    sum_of_all_depths = (
        sum_of_depths
        + left_tree_info.sum_of_all_depths
        + right_tree_info.sum_of_all_depths
    )

    return TreeInfo(num_nodes_in_tree, sum_of_depths, sum_of_all_depths)
