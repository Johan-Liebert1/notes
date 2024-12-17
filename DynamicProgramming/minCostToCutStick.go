package dynamicprogramming

import (
	"fmt"
	"sort"
)

func getKey(i, j int) string {
	// always make sure to separate these my commas as
	// (2,22) will give the same result as (22,2) if used without any separator
	return fmt.Sprintf("%d,%d", i, j)
}

func findMin(stickStart, stickEnd int, cuts []int, cache map[string]int) int {
	if stickEnd-stickStart <= 1 {
		return 0
	}

	key := getKey(stickStart, stickEnd)
	if v, ok := cache[key]; ok {
		return v
	}

	minCost := 1<<31 - 1

	for _, cut := range cuts {
		if cut <= stickStart || cut >= stickEnd {
			continue
		}

		// cut the stick at this point
		cost := stickEnd - stickStart
		left := findMin(stickStart, cut, cuts, cache)
		right := findMin(cut, stickEnd, cuts, cache)

		minCost = min(minCost, cost+left+right)
	}

	// if not valid cut is found, cost for this range will be 0
	if minCost == 1<<31-1 {
		minCost = 0
	}

	cache[key] = minCost

	return minCost
}

func minCost(n int, cuts []int) int {
	mapp := map[string]int{}
	sort.Ints(cuts)
	return findMin(0, n, cuts, mapp)
}

func MinCostToCutStick(n int, cuts []int) (v int) {
	return minCost(n, cuts)
}
