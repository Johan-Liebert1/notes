package binarytrees

// A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
// A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
// 
// The path sum of a path is the sum of the node's values in the path.
// 
// Given the root of a binary tree, return the maximum path sum of any non-empty path.

func maxPathSum(root *TreeNode) int {
    maxSum := -(1 << 31)

    var dfs func(node *TreeNode) int

    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }

        // Recursively get the max sum on the left and right subtrees, discarding negative sums
        leftMax := max(0, dfs(node.Left))
        rightMax := max(0, dfs(node.Right))

        // Calculate the maximum path sum with the current node as the highest point
        maxSum = max(maxSum, node.Val + leftMax + rightMax)

        // Return the max path sum including the current node and either one of its children
        // becuase this function is supposed to get the right/left subtree max sums
        // we've already included the root, left and right in the maxSum equation above
        return node.Val + max(leftMax, rightMax)
    }

    dfs(root)
    return maxSum
}
