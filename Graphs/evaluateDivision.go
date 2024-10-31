package graphs

import "fmt"

// If we cannot determine the answer, send -1

// Input:
// equations = [["a","b"],["b","c"]],
// values = [2.0,3.0],
// queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

// Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

type Equations = map[string]map[string]float64

func findPath(numerator, denominator string, equations Equations) float64 {
	queue := []string{numerator}
	visited := map[string]bool{}

	parent := map[string]string{}

    visited[numerator] = true

	for len(queue) > 0 {
		n := queue[0]
		queue = queue[1:]

		for d := range equations[n] {
            if visited[d] {
                continue
            }

			parent[d] = n

            visited[d] = true

			if d == denominator {
				// found a path so break out of all loops
				queue = []string{}
				break
			}

			queue = append(queue, d)
		}
	}

	return calculatePath(numerator, denominator, parent, equations)
}

func calculatePath(from, to string, parent map[string]string, equations Equations) float64 {
	answer := 1.

	at := to

	for at != from {
		if val, ok := parent[at]; ok {
			// since path is reversed, we need to find val / at
			answer *= equations[val][at]

			at = val
		} else {
			return -1.
		}
	}

	return answer
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	answers := make([]float64, len(queries))

	eqs := Equations{}

	// if we have ["a", "b"] and values [2.0]

	// then we'll have { "a": { "b": 2.0 } }
	for i, eq := range equations {
		num, den := eq[0], eq[1]

		if _, ok := eqs[num]; ok {
			eqs[num][den] = values[i]
		} else {
			mapp := map[string]float64{}
			mapp[den] = values[i]

			eqs[num] = mapp
		}

		if _, ok := eqs[den]; ok {
			eqs[den][num] = 1. / values[i]
		} else {
			mapp := map[string]float64{}
			mapp[num] = 1. / values[i]

			eqs[den] = mapp
		}
	}

	// for all queries we basically need to check if there is a path from
	// numerator of query to denominator of query

	for i, q := range queries {
		numerator, denominator := q[0], q[1]

		numeratorEqs, numExists := eqs[numerator]
		_, denExists := eqs[denominator]

		if !numExists || !denExists {
			answers[i] = -1.
			continue
		}

		if val, ok := numeratorEqs[denominator]; ok {
			answers[i] = val
			continue
		}

		answers[i] = findPath(numerator, denominator, eqs)
	}

	return answers
}

func EvaluateDivision() {
	answers := calcEquation(
		[][]string{{"x1", "x2"}, {"x2", "x3"}, {"x3", "x4"}, {"x4", "x5"}},
		[]float64{3.0, 4.0, 5.0, 6.0},
		[][]string{
			{"x1", "x5"},
			{"x5", "x2"},
			{"x2", "x4"},
			{"x2", "x2"},
			{"x2", "x9"},
			{"x9", "x9"},
		},
	)

	fmt.Printf("answers: %+v\n", answers)
}
