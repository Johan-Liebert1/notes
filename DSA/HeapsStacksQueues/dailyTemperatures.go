package heapsstacksqueues

// Given an array of integers temperatures represents the daily temperatures,
// return an array answer such that answer[i] is the number of days you have to wait after the ith
// day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
//
// Example 1:
//
// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]
// Example 2:
//
// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]

func dailyTemperatures(temp []int) []int {
	stack := []int{}

	answer := make([]int, len(temp))

	for i := len(temp) - 1; i >= 0; i-- {
		s := len(stack) - 1

		for s >= 0 && temp[stack[s]] <= temp[i] {
			stack = stack[:len(stack)-1]
			s--
		}

		if len(stack) == 0 {
			stack = append(stack, i)
			continue
		}

		answer[i] = stack[len(stack)-1] - i
		stack = append(stack, i)
	}

	return answer
}
