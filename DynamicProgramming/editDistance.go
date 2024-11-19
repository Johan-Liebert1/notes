package dynamicprogramming

import "fmt"

func getMinDist(word1 string, word2 string, i int, j int, cache [][]int) int {
	if j >= len(word2) {
		// j has reached the end of word1 (i.e., we've processed all characters in word2),
		//  but we still MIGHT have characters left in word1 starting from index i.
		return len(word1) - i
	}

	if i >= len(word1) {
		// i has reached the end of word1 (i.e., we've processed all characters in word1),
		//  but we still have characters left in word2 starting from index j.
		return len(word2) - j
	}

	if cache[i][j] != -1 {
		return cache[i][j]
	}

	// both letters are the same, we can just move forward
	if word1[i] == word2[j] {
		val := getMinDist(word1, word2, i+1, j+1, cache)

		cache[i][j] = val

		return val
	}

	// we have 3 options at any point in time

	// And we have to check each and every case

	// for example "eat" and "sea"

	// quickest is to remove "s" and append "t"
	// but if we put some check like
	// if len(word1) > len(word2) { /* delete char */ }
	// then we miss out on the delete

	// we can insert a character (only if word1.len < word2.len)
	// we can delete a character (only if word1.len > word2.len)
	// we can replace a characer (can do anytime)

	// we move i and we also move j as we just inserted
	// word2[j] at word1[i] so definitely word1[i] == word2[j]
	insertDist := 1 + getMinDist(word1, word2, i, j+1, cache)

	// removing is basically we didn't get a match on word1[i] and word2[j]
	// so we move to word[i + 1] but stay at word2[j]
	removeDist := 1 + getMinDist(word1, word2, i+1, j, cache)

	replaceDist := 1 + getMinDist(word1, word2, i+1, j+1, cache)

	cache[i][j] = min(insertDist, removeDist, replaceDist)

	return cache[i][j]
}

func minDistance(word1 string, word2 string) int {
	cache := [][]int{}

	for range len(word1) {
		thingy := make([]int, len(word2))

		for i := range len(word2) {
			thingy[i] = -1
		}

		cache = append(cache, thingy)
	}

	return getMinDist(word1, word2, 0, 0, cache)
}

func main() {
	minDist := minDistance("horse", "ros")

	fmt.Println("minDist: ", minDist)
}
