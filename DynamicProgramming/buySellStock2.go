package dynamicprogramming

func profit(prices []int, index int, lastBought int, cache [][]int) int {
	if index >= len(prices) {
		return 0
	}

    state := 0

    if lastBought != -1 {
        state = 1
    }

    if cache[state][index] != -1 {
        return cache[state][index]
    }

	buy := 0
	sell := 0

	nothing := profit(prices, index+1, lastBought, cache)

	// can only buy if we haven't already bought
	if lastBought == -1 {
		buy = -prices[index] + profit(prices, index+1, index, cache)
	}

	if lastBought != -1 {
		sell = prices[index] + profit(prices, index+1, -1, cache)
	}

	maxProfit := max(buy, sell, nothing)

    cache[state][index] = maxProfit

	return maxProfit
}

func maxProfit(prices []int) int {
    cache := make([][]int, 2)

    for i := range 2 {
        p := make([]int, len(prices))

        for j := range len(p) {
            p[j] = -1
        }

        cache[i] = p
    }

	return profit(prices, 0, -1, cache)
}
