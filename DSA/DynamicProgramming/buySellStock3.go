package dynamicprogramming

func profit3(prices []int, index, lastBought, remainingTransactions int, cache [][][]int) int {
	if index >= len(prices) {
		return 0
	}

	if cache[lastBought][remainingTransactions][index] != -1 {
		return cache[lastBought][remainingTransactions][index]
	}

	nothing := profit3(prices, index+1, lastBought, remainingTransactions, cache)

	buy := 0
	sell := 0

	if lastBought == 0 && remainingTransactions > 0 {
		buy = -prices[index] + profit3(prices, index+1, 1, remainingTransactions-1, cache)
	}

	if lastBought != 0 {
		sell = prices[index] + profit3(prices, index+1, 0, remainingTransactions, cache)
	}

	profit := max(buy, sell, nothing)

	cache[lastBought][remainingTransactions][index] = profit

	return profit
}

func buySellStock3(prices []int) int {
	cache := make([][][]int, 2) // for lastBought (0 or 1)

	for i := range 2 {
		cache[i] = make([][]int, 3) // for remaining transactions 0, 1, 2

		for j := range cache[i] {
			cache[i][j] = make([]int, len(prices))

			for k := range cache[i][j] {
				cache[i][j][k] = -1
			}
		}
	}

	return profit3(prices, 0, 0, 2, cache)
}

func buySellStock3DP(prices []int) int {
	cache := make([][][]int, 2) // for lastBought (0 or 1)

	for i := range 2 {
		cache[i] = make([][]int, 3) // for remaining transactions 0, 1, 2

		for j := range cache[i] {
			cache[i][j] = make([]int, len(prices)+1)
		}
	}

	for index := len(prices) - 1; index >= 0; index-- {
		for remainingTransactions := 2; remainingTransactions >= 0; remainingTransactions-- {
			for lastBought := 0; lastBought <= 1; lastBought++ {
				// profit3(prices, index+1, lastBought, remainingTransactions, cache)
				nothing := cache[lastBought][remainingTransactions][index+1]

				buy := 0
				sell := 0

				if lastBought == 0 && remainingTransactions > 0 {
					// profit3(prices, index+1, 1, remainingTransactions-1, cache)
					buy = -prices[index] + cache[1][remainingTransactions-1][index+1]
				}

				if lastBought != 0 {
					// profit3(prices, index+1, 0, remainingTransactions, cache)
					sell = prices[index] + cache[0][remainingTransactions][index+1]
				}

				profit := max(buy, sell, nothing)

				cache[lastBought][remainingTransactions][index] = profit
			}
		}
	}

	// cache[not bought][transactions completed][day]

	// so basically on the 0th day, nothing bought and 2 transactions completed
	return cache[0][2][0]
}

func buySellStock3SpaceOptmisied(prices []int) int {
	current := make([][]int, 2)
	next := make([][]int, 2)

	for i := range 2 {
		current[i] = make([]int, 3)
		next[i] = make([]int, 3)
	}

	for index := len(prices) - 1; index >= 0; index-- {
		for remainingTransactions := 2; remainingTransactions >= 0; remainingTransactions-- {
			for lastBought := 0; lastBought <= 1; lastBought++ {
				// profit3(prices, index+1, lastBought, remainingTransactions, cache)
				nothing := next[lastBought][remainingTransactions]

				buy := 0
				sell := 0

				if lastBought == 0 && remainingTransactions > 0 {
					// profit3(prices, index+1, 1, remainingTransactions-1, cache)
					buy = -prices[index] + next[1][remainingTransactions-1]
				}

				if lastBought != 0 {
					// profit3(prices, index+1, 0, remainingTransactions, cache)
					sell = prices[index] + next[0][remainingTransactions]
				}

				profit := max(buy, sell, nothing)

				current[lastBought][remainingTransactions] = profit
			}
		}

        next = current;
	}

    // next[haven't bought anything][2 transactions remaining]
	return next[0][2]
}
