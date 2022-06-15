from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []

        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return

            if len(array) < depth:
                array.append([node.val])
            else:
                array[depth - 1].append(node.val)

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 1)

        return array
