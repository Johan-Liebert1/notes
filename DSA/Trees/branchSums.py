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


def branch_sums(root: BST, array: List[int], current_sum: int = 0):
    if not root.left and not root.right:
        # leaf node, add the sum to array
        array.append(current_sum + root.value)

    if root.left:
        branch_sums(root.left, array, current_sum + root.value)

    if root.right:
        branch_sums(root.right, array, current_sum + root.value)


arr = []

branch_sums(newBst, arr)

print(arr)
