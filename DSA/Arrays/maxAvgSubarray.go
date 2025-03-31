package arrays

import "fmt"

func findMaxAverage(nums []int, k int) float64 {
	if len(nums) < k {
		return 0.0
	}

	left := 0
	right := k - 1

	lastSum := 0

	for i := left; i <= right; i++ {
		lastSum += nums[i]
	}

	maxAvg := float64(lastSum) / float64(k)

	left++
	right++

	for right < len(nums) {
		lastSum -= nums[left-1]
		lastSum += nums[right]

		lastAvg := float64(lastSum) / float64(k)

		if lastAvg > maxAvg {
			maxAvg = lastAvg
		}

		left++
		right++
	}

	return maxAvg
}

func main() {
	fmt.Println(findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4))
}
