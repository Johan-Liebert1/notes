package main

import (
	"coding-questions/miscellaneous"
	"fmt"
)

func main()  {
    allPerms := miscellaneous.Permutations([]int{1, 2, 3})
    fmt.Printf("%+v", allPerms)
}
