package arrays

func maxSubarraySumCircular(nums []int) int {
    globalMaxSum, globalMinSum := nums[0], nums[0]
    currMaxSum, currMinSum := 0, 0
    total := 0

    for _, n := range nums {
        // basically to add current number to the max sum, or start a new sum altogether
        // this is analogous to if sum < 0 { sum = 0 }
        currMaxSum = max(currMaxSum + n, n)

        // basically to add current number to the min sum, or start a new sum altogether
        currMinSum = min(currMinSum + n, n)

        total += n

        globalMaxSum = max(globalMaxSum, currMaxSum)
        globalMinSum = min(globalMinSum, currMinSum)
    }

    if globalMaxSum > 0 {
        // there was atleast one positive value in the input array
        return max(globalMaxSum, total - globalMinSum)
    }

    return globalMaxSum
}
