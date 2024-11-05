package main

import (
	"fmt"
	"slices"
	"strings"
)

func main() {
	s := "foobarfoobar"
	fmt.Println(s[6:])

    allPerms := []string{"foobar", "barfoo"}

    answer := []int{}

	for _, substr := range allPerms {
		i := 0

		for i+len(substr) <= len(s) {
			idx := strings.Index(s[i:], substr)

            fmt.Printf("idx: %d, s[%d:] = %s, substr: %s\n", idx, i, s[i:], substr)

			if idx == -1 {
				break
			}

			// we found the substring in the string
			if !slices.Contains(answer, idx+i) {
				answer = append(answer, idx+i)
			}

			i = idx + i + len(substr)

            fmt.Printf("i: %d\n\n", i)
		}

	}
}
