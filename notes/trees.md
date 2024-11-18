## Lowest common binary tree ancestor

root, node1, node2

#### Approach 1

We can first check if `node1` is to the left of `root` or to the right
We can again check the same for `node2`

if `node1` is on the left and `node2` on right, then `root` is the LCA

if `node1` and `node2` both are on the left, the we can ignore the entire right tree and then make `root.Left` as the new node and recursively try


#### Approach 2

We can calculate the path to node1 and node2 from the root
Then we can iterate both path arrays at once, and whereever they diverge, the element to the left of that will be their LCA

If they don't diverge then one of them is the LCA, which we can find by checking the smaller path

          3
       /     \
      5       1
     /  \    /   \
    6    2  0     8
        /   \
       7     4
                    

#### if we want the LCA of 6 and 2

the paths will be `[3, 5, 6]` and `[3, 5, 2]`

They diverge after `5`, so `5` is LCA


#### if we want the LCA of 5 and 7

the paths will be `[3, 5]` and `[3, 5, 2, 7]`

They don't diverge, so the last element of the smaller path is the LCA

## Path Sum 3

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

![LIS Decision tree](./pathsum3.jpg) 

#### Solution 1 (At each node get all the path sums)

```go
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
```

#### Solution 2 (Keep track of prefix sum in a hash map)

```go
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
```

## Max Path sum

Find the maximum path sum in a binary tree. A path can be `root.Left + root + root.Right`

```go
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
```
