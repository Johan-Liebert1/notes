package main

// Given an integer array nums, return true if there exists a triple of indices (i, j, k)
// such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
//
// Example 1:
//
// Input: nums = [1,2,3,4,5]
// Output: true
// Explanation: Any triplet where i < j < k is valid.

func triplet(nums []int, index int, prevIndex int, currElementNum int, table *[][]int) bool {
	if index == len(nums) {
		return false
	}

	if prevIndex != -1 && (*table)[index][prevIndex + 1] != -1 {
		v := (*table)[index][prevIndex]

		if v == 1 {
			return true
		} else {
			return false
		}
	}

	take := false

	// take the current number at the index
	if prevIndex == -1 || nums[index] > nums[prevIndex] {
		if currElementNum == 2 {
			return true
		}

		take = triplet(nums, index+1, index, currElementNum+1, table)
	}

	notTake := triplet(nums, index+1, prevIndex, currElementNum, table)

    v := 0

    if take || notTake {
        v = 1
    }

    (*table)[index][prevIndex + 1] = v

	return take || notTake
}

func increasingTriplet(nums []int) bool {
	table := [][]int{}

	for range len(nums) {
		arr := make([]int, len(nums))

		for i := range len(nums) {
			arr[i] = -1
		}

		table = append(table, arr)
	}

	return triplet(nums, 0, -1, 0, &table)
}

func main2() {
	print(increasingTriplet([]int{2, 1, 5, 0, 4, 6}))
}
