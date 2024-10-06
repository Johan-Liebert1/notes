package trees

// Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
// The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


func findSumFromRoot(root *TreeNode, currentSum, targetSum int) int {
	if root == nil {
		return 0
	}

	totalPaths := 0

	if currentSum+root.Val == targetSum {
		totalPaths += 1
	}

	return (totalPaths +
		findSumFromRoot(root.Left, currentSum+root.Val, targetSum) +
		findSumFromRoot(root.Right, currentSum+root.Val, targetSum))
}

func pathSum3BruteForce(root *TreeNode, targetSum int) int {
	if root == nil {
		return 0
	}

	return (pathSum3BruteForce(root.Left, targetSum) +
		pathSum3BruteForce(root.Right, targetSum) +
		findSumFromRoot(root, 0, targetSum))
}

func pathSumFast(root *TreeNode, currentSum, targetSum int, lookup map[int]int) int {
	totalPaths := 0

	if root == nil {
		return totalPaths
	}

	currentSum += root.Val

	if currentSum == targetSum {
		totalPaths++
	}

	// if the target sum is 8, and say the current sum is 15
	// then we basically check if we ever found a sum that was
	// 15 - 8 = 7
	//
	// if we ever had 7 as a sum, then we could've subtracted from 15
	// to get 8, which is the actual sum
	totalPaths += lookup[currentSum-targetSum]

	lookup[currentSum]++

	totalPaths += pathSumFast(root.Left, currentSum, targetSum, lookup)
	totalPaths += pathSumFast(root.Right, currentSum, targetSum, lookup)

	lookup[currentSum]--

	return totalPaths
}

func pathSum3(root *TreeNode, targetSum int) int {
	// maintain a prefix sum in a hash map
	// which contains how many times did we encounter a particular sum
	lookup := map[int]int{}

	return pathSumFast(root, 0, targetSum, lookup)
}
