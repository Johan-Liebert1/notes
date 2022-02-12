_ = """

given a binary tree, flatten it. Flattening = converting the tree into a linked list inorder traversal of the tree 

                8
              /   \
             3     10
            / \   /  \      ===>  1 <=> 3 <=> 4 <=> 6 <=> 7 <=> 8 <=> 9 <=> 10 <=> 14
           1   6  9  14
              / \
             4   7 

and then return the first element of the resulting list

"""

from BSTTraversal import Node


def flatten_binary_tree(root: Node) -> Node:
    # Right most node of the left tree connects to the current node
    # current node connects to the left most node of the right tree
    left_most, _ = flatten_tree_helper(root)
    return left_most


def flatten_tree_helper(root: Node) -> list[Node]:
    if root.left is None:
        left_most = root
    else:
        left_subtree_left_most, left_subtree_right_most = flatten_tree_helper(root.left)

        connect_nodes(left_subtree_right_most, root)
        left_most = left_subtree_left_most

    if root.right is None:
        right_most = root
    else:
        right_subtree_left_most, right_subtree_right_most = flatten_tree_helper(
            root.left
        )

        connect_nodes(root, right_subtree_left_most)
        right_most = right_subtree_right_most

    return [left_most, right_most]


def connect_nodes(left: Node, right: Node):
    left.right = right
    right.left = left
