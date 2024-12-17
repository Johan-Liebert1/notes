package main

import (
	dynamicprogramming "coding-questions/DynamicProgramming"
	"fmt"
)

func main() {
    i := []int{1, 3, 4, 5}
    minn := dynamicprogramming.MinCostToCutStick(7, i)

    fmt.Println(minn)

    fmt.Printf("'%s'\n", fmt.Sprint(i))
}
