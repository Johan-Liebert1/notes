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


def all_kinds_of_node_depths(rootNode: Node):
    array = [0]

    depth_calculator(rootNode, array)


def depth_calculator(root: Node, array: "list[int]", depth=0):
    pass
