package graphs

import (
	"fmt"
	"slices"
)

func minReorder(n int, connectionsParam [][]int) int {
	allConnections := map[int][]int{}
	directedConnections := map[int][]int{}

	for _, conn := range connectionsParam {
		start, end := conn[0], conn[1]

		directedConnections[start] = append(directedConnections[start], end)

		allConnections[start] = append(allConnections[start], end)
		allConnections[end] = append(allConnections[end], start)
	}

	reroutes := 0

	queue := []int{0}

	visited := make([]bool, n)
	visited[0] = true

	for len(queue) > 0 {
		city := queue[0]
		queue = queue[1:]

		for _, neighbor := range allConnections[city] {
			if visited[neighbor] {
				continue
			}

			visited[neighbor] = true
			queue = append(queue, neighbor)

			// If the original direction is from city to neighbor, it needs rerouting
			// We can do this as the graph only has n-1 edges, if it didn't we couldn't do this
			if slices.Contains(directedConnections[city], neighbor) {
				reroutes++
			}
		}
	}

	return reroutes
}

func ReorderPathsToReachCityZero() {
	minR := minReorder(6, [][]int{{0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}})

	fmt.Printf("Min Reorders: %d\n", minR)
}
