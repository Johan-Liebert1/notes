package miscellaneous

import (
	"slices"
)

// Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
//
// Only numbers 1 through 9 are used.
// Each number is used at most once.
// Return a list of all possible valid combinations. The list must not contain the same combination twice,
// and the combinations may be returned in any order.

// Input: k = 3, n = 9
// Output: [[1,2,6],[1,3,5],[2,3,4]]
// Explanation:
// 1 + 2 + 6 = 9
// 1 + 3 + 5 = 9
// 2 + 3 + 4 = 9
// There are no other valid combinations.

import "fmt"

func getKey(currentNums []int) string {
	s := ""

	for _, c := range currentNums {
		s += fmt.Sprint(c)
	}

	return s
}

func addComboToMap(currentNums []int, set map[string]bool) {
	newNums := make([]int, len(currentNums))
	copy(newNums, currentNums)

	for range len(currentNums) {
		key := getKey(currentNums)

		set[key] = true

		// now we rotate the array
		currentNums = append([]int{currentNums[len(currentNums)-1]}, currentNums...)
		currentNums = currentNums[:len(currentNums)-1]
	}
}

func combinationExists(currentNums []int, set map[string]bool) bool {
	_, ok := set[getKey(currentNums)]

	return ok
}

func CombinationSum3(numbersRequired int, sumTarget int) [][]int {
	sums := [][]int{}

	set := map[string]bool{}

	var findCombinations func(currentSum int, current []int)

	findCombinations = func(currentSum int, currentNums []int) {
		if len(currentNums) > numbersRequired || currentSum > sumTarget {
			return
		}

		if currentSum == sumTarget &&
			len(currentNums) == numbersRequired &&
			!combinationExists(currentNums, set) {

			addComboToMap(currentNums, set)

			newArray := make([]int, len(currentNums))
			copy(newArray, currentNums)
			sums = append(sums, newArray)
			return
		}

		for i := 1; i < 9; i++ {
			if sumTarget-i >= 1 && !slices.Contains(currentNums, i) {
				currentNums = append(currentNums, i)

				findCombinations(currentSum+i, currentNums)

				// backtrack regardless
				currentNums = currentNums[:len(currentNums)-1]
			}
		}

		return
	}

	for i := 1; i < 9; i++ {
		findCombinations(i, []int{i})
	}

	return sums
}
