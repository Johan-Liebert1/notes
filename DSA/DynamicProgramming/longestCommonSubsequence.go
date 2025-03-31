package dynamicprogramming

func lcs(text1 *string, text2 *string, i int, j int, table *[][]int) int {
	if i == len(*text1) || j == len(*text2) {
		return 0
	}

	if (*table)[i][j] != -1 {
		return (*table)[i][j]
	}

	if (*text1)[i] == (*text2)[j] {
		val := 1 + lcs(text1, text2, i+1, j+1, table)

		(*table)[i][j] = val

		return val
	}

	left := lcs(text1, text2, i+1, j, table)
	right := lcs(text1, text2, i, j+1, table)

	val := max(left, right)

	(*table)[i][j] = val

	return val
}

// return the length of the lcs
func longestCommonSubsequence(text1 string, text2 string) int {
	table := [][]int{}

	for range len(text1) {
		another := make([]int, len(text2))

		for i := range len(text2) {
			another[i] = -1
		}

		table = append(table, another)
	}

	return lcs(&text1, &text2, 0, 0, &table)
}
