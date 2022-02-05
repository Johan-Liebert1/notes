from typing import List
from constructionOfBST import BST

newBst = BST(25)
(
    newBst.insert(20)
    .insert(30)
    .insert(15)
    .insert(24)
    .insert(27)
    .insert(50)
    .insert(10)
    .insert(17)
    .insert(40)
    .insert(80)
)

# find the depth o every node in the binary tree and sum them all up
def node_depths(root: BST, current_depth=1, depth_sum: List[int] = [0]):
    if not root.left and not root.right:
        depth_sum[0] += current_depth

    if root.left:
        node_depths(root.left, current_depth + 1, depth_sum)

    if root.right:
        node_depths(root.right, current_depth + 1, depth_sum)

    return depth_sum[0]


print(node_depths(newBst))
