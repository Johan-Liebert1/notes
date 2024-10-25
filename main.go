package main

import (
	"coding-questions/miscellaneous"
	"fmt"
)

func main()  {
    allPerms := miscellaneous.PermutationsBySwapping([]int{1, 2, 3})
    allPerms2 := miscellaneous.Permutations([]int{1, 2, 3})

    fmt.Printf("%+v\n", allPerms)
    fmt.Printf("%+v", allPerms2)
}
