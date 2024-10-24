package miscellaneous

// Iterate over the array and we keep track of which array elements we have used up in our Permutation
func Permutations(array []int) [][]int {
	allPerms := [][]int{}

	takenIndexMap := make([]int, len(array))

	var findPerms func(current []int)

	findPerms = func(current []int) {
		if len(current) == len(array) {
			newArray := make([]int, len(array))
			copy(newArray, current)

			allPerms = append(allPerms, newArray)
			return
		}

		for i, c := range array {
			// has not been taken, we can take this
			if takenIndexMap[i] == 0 {
				takenIndexMap[i] = 1
				current = append(current, c)

				findPerms(current)

				current = current[:len(current)-1]
				takenIndexMap[i] = 0
			}
		}
	}

	for i, c := range array {
		takenIndexMap[i] = 1
		findPerms([]int{c})
		takenIndexMap[i] = 0
	}

	return allPerms
}
