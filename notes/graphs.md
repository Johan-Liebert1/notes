## Delete from middle of linked list

### Easy way
Traverse linked list twice, once to find the length and once to delete the middle

### Have a slow pointer and a fast pointer. The fast pointer moves twice as fast as the slow one

So, when the fast ptr is at the end, the slow pointer will be directly in the middle


Example


```
LL -> 1, 2, 3, 4, 5

Iter 1
slow = 1, fast = 1

Iter 2
slow = 2, fast = 3

Iter 3
slow = 3, fast = 5
```

## Copying an array in go

```go
newArray := make([]Type, len(arrayToCopy))
copy(newArray, arrayToCopy)
```

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
