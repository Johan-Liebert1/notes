from binaryTree import BinaryTree, Node

_ = """  
A path in a binary tree is a chain of nodes where every node is connected to at most two other nodes.

    1
  /   \
  2    3
 / \  / \
4   5 7  8

paths in above tree 

4 -> 2 -> 5
4 -> 2 > 1 -> 3 -> 8
4 -> 2 > 1 -> 3 -> 7
5 -> 2 > 1 -> 3 -> 7

not a path
4 -> 2 -> 5 -> 1 as 2 is connected to 3 nodes

Find the max path sum
"""

tree = BinaryTree()

for i in range(1, 9):
    tree.insert(i)


def max_path_helper(current_node: Node) -> "tuple[int, int]":
    """
    1. Get the left branch sum of the current node
    2. Get the right branch sum of the current node
    3. Get the sum of right branch, left branch and the current node's value
    """
    if not current_node:
        return 0, 0

    sum_left_branch, max_sum_left_path = max_path_helper(current_node.left)
    sum_right_branch, max_sum_right_path = max_path_helper(current_node.right)

    # this could be negative
    max_child_sum_as_branch = max(sum_left_branch, sum_right_branch)

    value = current_node.value

    # taking the max as max_child_sum_as_branch could be negative
    max_sum_as_branch = max(max_child_sum_as_branch + value, value)

    # max sum using the parent node
    max_sum_as_tree = max(sum_left_branch + value + sum_right_branch, max_sum_as_branch)

    running_max_path_sum = max(max_sum_left_path, max_sum_right_path, max_sum_as_tree)

    return max_sum_as_branch, running_max_path_sum


def max_path_sum(root: Node):
    _, max_sum = max_path_helper(root)

    return max_sum


print(max_path_sum(tree.root))
