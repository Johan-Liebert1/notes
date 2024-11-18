package main

import (
	"coding-questions/greedy"
	"fmt"
)

func main() {
    ans := greedy.LeastInterval([]byte{'A','C','A','B','D','B'}, 1)
    fmt.Printf("ans: %d\n", ans)
}
