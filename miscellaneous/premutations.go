package miscellaneous

// Iterate over the array and we keep track of which array elements we have used up in our Permutation
// We use an extra map here to keep track of all the indicies we've already added in our Permutations

// let's say the array is [a, b, c] and our current Permutations array is []
// we iterate over the entire array and append the element into current if the element is not in our map
// we append a in there so current is now [a] and we add 0 to map, so map is [1, 0, 0] -> 1 at 0th idx means we have used it up

// now we recursively call the function.
// we still iterate from 0, but since 0th index in map is 1, we won't take the 0th index
// so we append b in current. Now current is [a, b] and map is [1, 1, 0]

// we recursively call the function again now adding c, so now current is [a, b, c] and map is [1, 1, 1]
// since len(current) == len(array), we return and store this Permutation

// while backtracking, we now remove c from the map and from the current array
// then, backtracking at index b, we remove b from map, and add c in it's place
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

	findPerms([]int{})

	return allPerms
}

// let's say array is [a, b, c]
// we start iterating from index 0, which is a
// now, we will swap each element with a so that we get all permuations starting with a, b and c 
// as we will at one point swap a with a, a with b and a with c

// then we recursively call the function passing index as 1
// we have 3 possibilities now as [a, b, c], [b, a, c], [c, b, a] as we swapped a with every other element once
// we perform the same swapping thing, but now starting at index 1, which is starting at b

// this way we get all permutations where 0th index is a, b and c, and
// where 1st index is a, b and c, 2nd index is a, b and c and so on
func PermutationsBySwapping(array []int) [][]int {
	allPerms := [][]int{}

	var findPerms func(currentPerm []int, index int)

	findPerms = func(currentPerm []int, index int) {
		if index >= len(currentPerm) {
			newArray := make([]int, len(currentPerm))

			copy(newArray, currentPerm)

			allPerms = append(allPerms, newArray)
			return
		}

		for i := index; i < len(currentPerm); i++ {
			// we swap the elements
			currentPerm[i], currentPerm[index] = currentPerm[index], currentPerm[i]

			findPerms(currentPerm, index+1)

            // undo swapping as we are passing the same array to the function
			currentPerm[i], currentPerm[index] = currentPerm[index], currentPerm[i]
		}
	}

	findPerms(array, 0)

	return allPerms
}
