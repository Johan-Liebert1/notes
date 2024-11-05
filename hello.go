package main

func minSubArrayLen(target int, nums []int) int {
	minSize := 1<<31 - 1

	first, second := 0, 1

	currentSum := nums[first]

	if currentSum >= target {
		return 1
	}

	if len(nums) > 1 {
		currentSum += nums[second]
	}

	for second < len(nums) {
		if nums[second] >= target {
			return 1
		}

		if currentSum >= target {
			minSize = min(minSize, second-first+1)

			currentSum -= nums[first]

			first++
		} else {
			second++

			if second < len(nums) {
				currentSum += nums[second]
			}
		}
	}

	if minSize == 1<<31-1 {
		return 0
	}

	return minSize
}
