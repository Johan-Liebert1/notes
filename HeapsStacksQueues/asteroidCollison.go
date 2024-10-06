// We are given an array asteroids of integers representing asteroids in a row.
//
// For each asteroid, the absolute value represents its size, and the sign represents its direction
// (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
//
// Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
// If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

package heapsstacksqueues

import "math"

func asteroidCollision(asteroids []int) []int {
	i := 1
	o := 0

	inPlace := false

	output := []int{asteroids[0]}

	for i < len(asteroids) {
		if len(output) == 0 {
			output = append(output, asteroids[i])
			o = 0
			i++
			continue
		}

		inPlace = false
		current := output[o]
		next := asteroids[i]

		if next < 0 && current > 0 {
			// one of them is negative
			// and they are moving towards each other
			for next < 0 && current > 0 {
				final := 0

				if current+next != 0 {
					if math.Abs(float64(next)) > math.Abs(float64(current)) {
						final = next
					} else {
						final = current
					}
				}

				if !inPlace {
					if final == 0 {
						// remove the last element if the next asteroid
						// is of the same size and moving towards us
						output = output[:len(output)-1]
					} else {
						output[o] = final
					}
				} else {
					toCutTill := len(output) - 1

					if final == 0 {
						toCutTill = len(output) - 2
					}

					// modifying output in place
					output = output[:toCutTill]
					o = len(output) - 1

					if final != 0 {
						output[len(output)-1] = final
					}
				}

				o--

				if o < 0 || o >= len(output)-1 {
					break
				}

				current = output[o]
				next = output[o+1]

				inPlace = true
			}

			o = len(output) - 1
			i++
			continue
		}

		output = append(output, next)
		o++
		i++
	}

	return output
}
