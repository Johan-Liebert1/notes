package arrays

import "fmt"

func minEatingSpeed(piles []int, h int) int {
	min, max := 1, -1

	for _, p := range piles {
		if p > max {
			max = p
		}
	}

	// now we simply simulate binary search
	for {
		k := min + (max-min)/2

		fmt.Println(k)

		// simulate eating bananas
		hours := 0

		for _, p := range piles {
			hours += (p / k)

			if p%k != 0 {
				hours++
			}
		}

		if hours == h {
			return k
		}

		// we finished them too quickly. Lower k
		if hours < h {
			max = k - 1
		} else {
			min = k + 1
		}
	}
}
