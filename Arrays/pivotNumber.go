package arrays

func pivotIndexMine(nums []int) int {
	if len(nums) == 1 {
		return 0
	}

	suffixSum := make([]int, len(nums))

	suffixSum[len(suffixSum)-1] = nums[len(nums)-1]

	for i := len(nums) - 2; i >= 0; i-- {
		suffixSum[i] += nums[i] + suffixSum[i+1]
	}

	if suffixSum[1] == 0 {
		return 0
	}

	for i := 1; i < len(nums)-1; i++ {
		nums[i] += nums[i-1]

		if nums[i-1] == suffixSum[i+1] {
			return i
		}
	}

	if nums[len(nums)-2] == 0 {
		return len(nums) - 1
	}

	return -1
}

func pivotIndex(nums []int) int {
	sum := 0

	for _, v := range nums {
		sum += v
	}

	left := 0

	right := sum

	for i, v := range nums {
		right -= v

		if left == right {
			return i
		}

		left += v

	}

	return -1
}
