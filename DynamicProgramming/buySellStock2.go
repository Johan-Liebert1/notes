package dynamicprogramming

func profit(prices []int, index int, lastBought int, cache [][]int) int {
	if index >= len(prices) {
		return 0
	}

	if cache[lastBought][index] != -1 {
		return cache[lastBought][index]
	}

	// we can either buy or sell
	buy := 0
	sell := 0

	// or do nothing
	nothing := profit(prices, index+1, lastBought, cache)

	// can only buy if lastBought == -1
	if lastBought == 0 {
		buy = -prices[index] + profit(prices, index+1, 1, cache)
	} else {
		sell = prices[index] + profit(prices, index+1, 0, cache)
	}

	maxProfit := max(buy, sell, nothing)

	cache[lastBought][index] = maxProfit

	return maxProfit
}

func maxProfitRecursion(prices []int) int {
	cache := [][]int{}

	for range 2 {
		arr := make([]int, len(prices))

		for i := range arr {
			arr[i] = -1
		}

		cache = append(cache, arr)
	}

	return profit(prices, 0, 0, cache)
}

func maxProfitIterative(prices []int) int {
	n := len(prices)
	if n == 0 {
		return 0
	}

	// Create a cache table
	cache := make([][]int, 2)

	for i := 0; i < 2; i++ {
		cache[i] = make([]int, n+1)
	}

	// Initialize base case: dp[0][n] and dp[1][n] = 0

    // don't really need to do this cause Go, but keeping it here for reference
	for i := 0; i < 2; i++ {
		cache[i][n] = 0
	}

	// Fill the dp table
	for index := n - 1; index >= 0; index-- {
		for lastBought := 0; lastBought < 2; lastBought++ {
            // simply copy the recurrence relation
			nothing := cache[lastBought][index+1]
			buy := 0
			sell := 0

			if lastBought == 0 {
				buy = -prices[index] + cache[1][index+1]
			} else {
				sell = prices[index] + cache[0][index+1]
			}

			cache[lastBought][index] = max(buy, sell, nothing)
		}
	}

	// The result is stored in dp[0][0]
	return cache[0][0]
}

// We can see in the iterative solution that we're only using two values
// so we don't really need an entire array
func maxProfit(prices []int) int {
    // these are like the [lastBought (0 | 1)][index + 1]
	futureNoStock, futureWithStock := 0, 0

	// Iterate backward through the prices
	for index := len(prices) - 1; index >= 0; index-- {
		// Compute the current states based on future states

        // profit if NO stock is held at index
		currentNoStock := max(futureNoStock, -prices[index]+futureWithStock)

        // profit if SOME stock is held at index
		currentWithStock := max(futureWithStock, prices[index]+futureNoStock)

		// Update future states for the next iteration
		futureNoStock, futureWithStock = currentNoStock, currentWithStock
	}

	// The result is the max profit starting at index 0 without holding stock
	return futureNoStock
}
