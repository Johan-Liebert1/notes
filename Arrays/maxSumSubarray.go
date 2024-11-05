package arrays

func maxSubArray(nums []int) int {
    // use Kadane's algo

    sum := 0
    maxSum := -((1<<31) - 1)

    for _, n := range nums {
        sum += n

        maxSum = max(maxSum, sum)
        sum = max(sum, 0)
    }

    return maxSum
}
