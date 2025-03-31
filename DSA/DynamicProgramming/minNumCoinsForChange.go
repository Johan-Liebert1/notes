package dynamicprogramming

import (
	"fmt"
)

// You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
//
// Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
//
// You may assume that you have an infinite number of each kind of coin.
//
//
//
// Example 1:
//
// Input: coins = [1,2,5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1
// Example 2:
//
// Input: coins = [2], amount = 3
// Output: -1
// Example 3:
//
// Input: coins = [1], amount = 0
// Output: 0

func coinChangeHelper(coins *[]int, amount int, array *[]int) int {
	if amount == 0 {
		return 0
	}

    if (*array)[amount] != 1<<31 - 1 {
        return (*array)[amount]
    }

	minCoins := 1<<31 - 1

	for _, coin := range *coins {
		if coin <= amount {
			c := coinChangeHelper(coins, amount-coin, array)

			if c >= 0 && c + 1 < minCoins {
				minCoins = c + 1
			}
		}
	}

    if minCoins == 1<<31 - 1 {
        minCoins = -1
    }

    (*array)[amount] = minCoins

	return minCoins
}

func coinChange(coins []int, amount int) int {
    array := make([]int, amount+1)

    for i := range amount + 1 {
        array[i] = 1<<31 - 1
    }

    return coinChangeHelper(&coins, amount, &array)
}

func coinChangeDP(coins []int, amount int) int {
	array := make([]int, amount+1)

	maxInt := (1 << 32) - 1

	for i := range amount + 1 {
		array[i] = maxInt
	}

	array[0] = 0

	for i := 1; i < amount+1; i++ {
		for _, coin := range coins {
			if i-coin < 0 {
				continue
			}

			if i-coin == 0 {
				array[i] = 1
			} else {
				array[i] = min(array[i], array[i-coin]+1)
			}
		}
	}

	if array[amount] == maxInt {
		return -1
	}

	return array[amount]
}

func main() {
	fmt.Println(coinChangeDP([]int{1, 2, 5}, 11))
}
