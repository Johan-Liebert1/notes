package dynamicprogramming

func lis(nums []int, prevIndex int, currIndex int) int {
	n := len(nums)

	if currIndex == n {
		return 0
	}

	// Case 1: Exclude the current element
	exclude := lis(nums, prevIndex, currIndex+1)

	// Case 2: Include the current element if it forms an increasing subsequence
	include := 0
	if prevIndex == -1 || nums[currIndex] > nums[prevIndex] {
		include = 1 + lis(nums, currIndex, currIndex+1)
	}

	// Return the maximum of both cases
	return max(exclude, include)
}

func lengthOfLIS(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	// Start recursion with -1 as prevIndex (no previous element)
	return lis(nums, -1, 0)
}
