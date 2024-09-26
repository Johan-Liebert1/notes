package main

// Given the root of a binary tree and an integer targetSum,
// return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
// Each path should be returned as a list of the node values, not node references.
//
// A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum2(root *TreeNode, targetSum int, currentSum int, array *[][]int, currentArray *[]int) {
	if root == nil {
		return
	}

	sum := currentSum + root.Val

	*currentArray = append(*currentArray, root.Val)

	defer func() {
		*currentArray = (*currentArray)[:len(*currentArray)-1]
	}()

	if root.Left == nil && root.Right == nil {
		if sum == targetSum {
			temp := make([]int, len(*currentArray))
			copy(temp, *currentArray)
			*array = append(*array, temp)

			return
		}

		return
	}

	// left
	pathSum2(root.Left, targetSum, sum, array, currentArray)

	pathSum2(root.Right, targetSum, sum, array, currentArray)
}

func pathSum(root *TreeNode, targetSum int) [][]int {
	array := [][]int{}

	currentArray := []int{}

	pathSum2(root, targetSum, 0, &array, &currentArray)

	return array
}
